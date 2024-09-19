import yt_dlp
import os


def download_playlist(playlist_url, ffmpeg_location="C:/Paths"):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": "%(title)s.%(ext)s",
    }

    if ffmpeg_location:
        ydl_opts["ffmpeg_location"] = ffmpeg_location

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    ffmpeg_path = input(
        "Enter the path to ffmpeg (leave blank if it's in PATH): "
    ).strip()

    if ffmpeg_path and os.path.exists(ffmpeg_path):
        download_playlist(playlist_url, ffmpeg_path)
    else:
        download_playlist(playlist_url)
