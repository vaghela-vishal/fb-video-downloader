
from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['url']
        output_path = 'static/fb_video.mp4'
        ydl_opts = {
            'outtmpl': output_path,
            'format': 'bestvideo+bestaudio/best',
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return render_template('index.html', downloaded=True, video_path=output_path)
    return render_template('index.html', downloaded=False)

if __name__ == '__main__':
    app.run(debug=True)
