# AudioPhoenix: YouTube to MP3 Transmogrifier

AudioPhoenix is a script that downloads a YouTube video, converts it to an MP3 format, adds ID3 tags and album art, renames the file, and moves it to a specified directory.

## Prerequisites

Before running AudioPhoenix, you need to install the following dependencies:

- yt-dlp: A command-line program to download videos from YouTube and other video sites.
- ffmpeg: A complete, cross-platform solution to record, convert and stream audio and video.

You can install these dependencies using the package manager of your operating system. For example, on Ubuntu, you can install them with the following commands:

```bash
sudo apt update
sudo apt install yt-dlp ffmpeg
```

## Usage 

to run AudioPhoenix, simple exeucite it with Python: 
``` bash
python audio_phoenix.py
```
Before running the sccript, make sure to replace the placeholders in the script with your actual values. For exampl, replace "INSERT YOUTUBE URL HERE" with the actual YouTube URL, "INSERT ALBUM ART URL HERE" with the URL of the album art image, and so on. Also, replace "INSERT SOURCE DIRECTORY HERE" and "INSERT DESTINATION DIRECTORY HERE" with the actual paths to your source and destination directories. The same goes for the ID3 tags (title, artist, album, etc.).

## Disclaimer

AudioPhoenix is intended for personal use only. Do not use it to download copyrighted material without permission from the copyright holder. The author of AudioPhoenix is not responsible for any misuse of this script.
