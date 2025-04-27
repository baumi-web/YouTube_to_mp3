import os
from pathlib import Path
import yt_dlp

def download_audio_as_mp3(youtube_url, save_name):
    downloads_path = str(Path.home() / "Downloads")  # Pfad zum Downloads-Ordner
    output_template = os.path.join(downloads_path, save_name + '.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,  # zeigt Fortschritt an
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    print(f"✅ Fertig! Gespeichert unter: {downloads_path}/{save_name}.mp3")

if __name__ == "__main__":
    url = input("Bitte YouTube-Link eingeben: ")
    save_name = input("Wie soll die MP3-Datei heißen? (Ohne .mp3 am Ende): ")
    download_audio_as_mp3(url, save_name)

