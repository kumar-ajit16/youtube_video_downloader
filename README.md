# youtube_video_downloader

A simple web-based YouTube video downloader built using **Flask** and **yt-dlp**.  
Users can paste a YouTube video link, click **Download**, and get the video saved locally.

---

## Features

- Paste YouTube link and download video
- Clean and minimal frontend
- Shows **Downloading…** while processing
- Shows **Video downloaded ✅** after completion
- Downloads only a single video (no playlist)
- Stable configuration to avoid 403 / empty file issues
- Uses progressive MP4 (no ffmpeg required)

---

## Tech Stack

- **Backend:** Python, Flask  
- **Downloader:** yt-dlp  
- **Frontend:** HTML, CSS, Vanilla JavaScript  

---


---

## Requirements

- Python 3.10 or higher  
- pip  
- Virtual environment (recommended)

---

## Installation & Setup

### 1. Create project directory
```bash
mkdir api
cd api
python -m venv venv
source venv/bin/activate

### 2. Install dependencies
pip install flask yt-dlp


