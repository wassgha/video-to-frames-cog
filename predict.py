from cog import BasePredictor, Input, Path
from typing import List
import subprocess
import os
import uuid
import shutil

class Predictor(BasePredictor):
    def predict(self,
                video: Path = Input(description="Video to split into frames"),
                fps: float = Input(description="Number of images per second of video, when not exporting all frames", default=1.0, ge=0.05),
                downsample: bool = Input(description="Downsample frames to a maximum of 480p", default=True),
    ) -> List[Path]:
        """Run ffmpeg to split the video into frames"""
        # Create a unique output directory for this prediction
        unique_id = str(uuid.uuid4())
        output_dir = f"/tmp/frames_{unique_id}"
        os.makedirs(output_dir, exist_ok=True)

        # Clean up any previous temp directories (optional, helps manage disk space)
        for dirpath in [d for d in os.listdir("/tmp") if d.startswith("frames_") and d != f"frames_{unique_id}"]:
            try:
                shutil.rmtree(os.path.join("/tmp", dirpath))
            except Exception:
                pass

        # Set scaling filter if downsampling is enabled
        scale_filter = "scale='min(iw,iw*480/ih)':'min(ih,480)':flags=lanczos" if downsample else ""
        
        # For fps extraction, combine fps and scale filters if both are needed
        if downsample:
            filters = f"fps={fps},{scale_filter}"
        else:
            filters = f"fps={fps}"
        command = f"ffmpeg -hwaccel cuda -i \"{video}\" -vf \"{filters}\" {output_dir}/out%03d.png"

        subprocess.run(command, shell=True, check=True)
        frame_files = sorted(os.listdir(output_dir))
        frame_paths = [Path(os.path.join(output_dir, frame_file)) for frame_file in frame_files]

        return frame_paths
