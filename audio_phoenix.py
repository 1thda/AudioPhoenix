"""
This script downloads a YouTube video, converts it to mp3, adds ID3 tags and album art,
renames the file, and moves it to a specified directory.
"""

import os
import shutil
import subprocess
from io import BytesIO

import requests
from PIL import Image
from mutagen.id3 import APIC, ID3, TALB, TBPM, TCON, TDRC, TIT2, TPE1, TPE2

# Define the URL of the YouTube video
URL = "INSERT YOUTUBE URL HERE"

# Use yt-dlp to download the video as a temporary file
subprocess.run(["yt-dlp", "--parse-metadata",
                "title:%(artist)s - %(title)s", "-f 140", "-o", "temp.%(ext)s", URL], check=True)

# Use ffmpeg to convert the temporary file to mp3
subprocess.run(["ffmpeg", "-i", "temp.m4a", "-c:a",
                "libmp3lame", "-q:a", "8", "output.mp3"], check=True)

# Delete the temporary file
os.remove("temp.m4a")

# URL of the album art image
URL_TO_IMAGE = 'INSERT ALBUM ART URL HERE'  # pylint: disable=line-too-long

# Download the album art and save it as 'album_art.jpg'
RESPONSE = requests.get(URL_TO_IMAGE, timeout=5)
IMG = Image.open(BytesIO(RESPONSE.content))
IMG.save('album_art.jpg')

# Create a Frame instance for the artist tag
TITLE = TIT2(encoding=3, text="INSERT TITLE HERE")
ARTIST = TPE1(encoding=3, text="INSERT ARTIST HERE")
ALBUM = TALB(encoding=3, text="INSERT ALBUM NAME HERE")
ALBUM_ARTIST = TPE2(encoding=3, text="INSERT ALBUM ARTIST HERE")
GENRE = TCON(encoding=3, text="INSERT GENRE HERE")
YEAR = TDRC(encoding=3, text="INSERT YEAR HERE")
BPM = TBPM(encoding=3, text="INSERT BPM HERE")

# Create an ID3 tag if it doesn't exist
AUDIO = ID3("output.mp3")

# Assign the Frame instance to the MP3 file
AUDIO.add(TITLE)
AUDIO.add(ARTIST)
AUDIO.add(ALBUM)
AUDIO.add(ALBUM_ARTIST)
AUDIO.add(GENRE)
AUDIO.add(YEAR)
AUDIO.add(BPM)

# Add album art
with open('album_art.jpg', 'rb') as albumart:
    AUDIO.add(APIC(
        encoding=3,
        mime='image/jpeg',
        type=3, desc='Cover',
        data=albumart.read()
    ))
AUDIO.save()

# Define your source and destination directories
SOURCE_DIR = "INSERT SOURCE DIRECTORY HERE"
DEST_DIR = "INSERT DESTINATION DIRECTORY HERE"

# Define your old and new filenames
OLD_FILENAME = "output.mp3"
NEW_FILENAME = str(TITLE) + '.mp3'

# Rename the file
os.rename(os.path.join(SOURCE_DIR, OLD_FILENAME),
          os.path.join(SOURCE_DIR, NEW_FILENAME))

# Move the renamed file and the album art to the Desktop
shutil.move(os.path.join(SOURCE_DIR, NEW_FILENAME),
            os.path.join(DEST_DIR, NEW_FILENAME))
shutil.move(os.path.join(SOURCE_DIR, "album_art.jpg"),
            os.path.join(DEST_DIR, "album_art.jpg"))
