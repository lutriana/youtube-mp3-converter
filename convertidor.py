import yt_dlp
import os

url = input("Pega el link de YouTube: ")

# Carpeta destino
carpeta = os.path.expanduser("~/Downloads/musica abuelito")

# Crear la carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
    'noplaylist': True,
    'quiet': False,
    'extractaudio': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])