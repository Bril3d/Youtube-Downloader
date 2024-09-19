import yt_dlp
import os


def download_playlist(playlist_url, format_choice, ffmpeg_location="C:/Paths"):
    ydl_opts = {
        "format": "bestaudio/best" if format_choice == "mp3" else "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
    }

    if format_choice == "mp3":
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    else:
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }]

    if ffmpeg_location:
        ydl_opts["ffmpeg_location"] = ffmpeg_location

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


def main():
    while True:
        playlist_url = input("Enter the YouTube playlist URL: ")
        format_choice = input("Choose format (mp3/mp4): ").lower()
        while format_choice not in ["mp3", "mp4"]:
            format_choice = input("Invalid choice. Please enter mp3 or mp4: ").lower()

        ffmpeg_path = input("Enter the path to ffmpeg (leave blank if it's in PATH): ").strip()

        if ffmpeg_path and os.path.exists(ffmpeg_path):
            download_playlist(playlist_url, format_choice, ffmpeg_path)
        else:
            download_playlist(playlist_url, format_choice)

        another = input("Do you want to download another playlist? (yes/no): ").lower()
        if another != "yes":
            break

    print("Thank you for using the playlist downloader!")


if __name__ == "__main__":
    main()
