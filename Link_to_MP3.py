from pytube import YouTube
import os
from pydub import AudioSegment
from pathlib import Path

def download_audio_as_mp3(youtube_url, save_name):
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()

    # Temporär herunterladen (aktuelles Verzeichnis)
    print("Lade herunter...")
    out_file = stream.download()

    # Pfade vorbereiten
    downloads_path = str(Path.home() / "Downloads")  # Downloads-Ordner des Benutzers
    mp3_file_path = os.path.join(downloads_path, save_name + ".mp3")

    print("Konvertiere in MP3...")
    audio = AudioSegment.from_file(out_file)
    audio.export(mp3_file_path, format="mp3")

    # Originaldatei löschen (optional)
    os.remove(out_file)

    print(f"Fertig! Gespeichert unter: {mp3_file_path}")

if __name__ == "__main__":
    url = input("Bitte YouTube-Link eingeben: ")
    save_name = input("Wie soll die MP3-Datei heißen? (Ohne .mp3 am Ende): ")
    download_audio_as_mp3(url, save_name)
