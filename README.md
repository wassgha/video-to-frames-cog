# Video to Frames

A utility for converting video files into individual frame images using ffmpeg.

## Description

This is a simple Cog model that takes a video file as input and extracts individual frames. You can either:
- Extract frames at a specific frame rate (e.g., 1 frame per second)
- Extract all frames from the video (may be slow for larger videos)

## Usage

### Online via Replicate

Use this model on [Replicate](https://replicate.com/wassgha/video-to-frames)

### Local Installation

To run this model locally, you'll need [Cog](https://github.com/replicate/cog) installed:

```bash
# Install Cog
curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_`uname -s`_`uname -m`
chmod +x /usr/local/bin/cog

# Clone this repository
git clone https://github.com/wassgha/video-to-frames
cd video-to-frames

# Run predictions
cog predict -i video=@path/to/your/video.mp4 -i fps=1
```

## API Options

- `video`: The video file to process
- `fps`: Number of frames to extract per second (default: 1)
- `extract_all_frames`: Set to true to extract every single frame (default: false)

## Examples

Extract 1 frame per second:
```bash
cog predict -i video=@my-video.mp4 -i fps=1
```

Extract 10 frames per second:
```bash
cog predict -i video=@my-video.mp4 -i fps=10
```

Extract all frames:
```bash
cog predict -i video=@my-video.mp4 -i extract_all_frames=true
```

## License

MIT
