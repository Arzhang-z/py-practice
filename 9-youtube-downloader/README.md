# YouTube Downloader (Python)

A simple command-line YouTube video downloader written in Python using **pytube**.  
Supports downloading progressive MP4 streams with a live progress bar.

---

## Features

- Download YouTube videos via URL
- Select video quality (e.g. `720p`, `360p`)
- Download highest available progressive MP4 by default
- Live download progress using `tqdm`
- Automatic output directory handling

---

## Requirements

- Python 3.8+
- Internet connection (obviously)

### Python Dependencies

Install dependencies with:

```bash
pip install -r requirememts.py
```

## Usage
Run the script from the command line:

```bash
python mian.py <url> [options]
```
#### Positional Arguments

- url
The YouTube video URL.

Optional Arguments

- -q, --quality
Video resolution (e.g. 720p, 480p).
Default: highest (highest available progressive MP4)

- -o, --output_path
Directory to save the downloaded video.
Default: current working directory.

#### Examples

Download the highest available quality:

```bash
python downloader.py https://www.youtube.com/watch?v=VIDEO_ID
```

Download a specific resolution:

```bash
python downloader.py https://www.youtube.com/watch?v=VIDEO_ID -q 720p
```

Download to a custom directory:

```bash
python downloader.py https://www.youtube.com/watch?v=VIDEO_ID -o ./videos
```
## Notes & Limitations

This downloader uses progressive streams only.

Maximum quality is typically 720p.

Higher resolutions (1080p+) require adaptive streams and audio/video merging, which is not implemented.

If a requested quality is not available, the download will abort with a message.

Some videos may be unavailable due to region, age restrictions, or copyright limitations.

## Project Structure
```
.
├── downloader.py
└── README.md
```
---
This project is for educational purposes only.
Ensure you comply with YouTube’s Terms of Service and applicable copyright laws when downloading content.