from flask import Flask, render_template, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    ydl_opts = {
        "format": "best[ext=mp4][protocol^=http]/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "noplaylist": True,
        "retries": 5,
        "fragment_retries": 5,
        "sleep_interval": 3,
        "max_sleep_interval": 6,
        "hls_use_mpegts": False,
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Download failed. Try again in a few seconds."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
