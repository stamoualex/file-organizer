# File Organizer

A Python script that automatically sorts files in a folder into subfolders by file type. 

## How to Run

1. Make sure Python is installed (python.org)
2. Download `file_organizer.py` from this repo
3. Open a terminal in the folder where the file is saved
4. Run this command:
   python file_organizer.py
5. Enter the path of the folder you want to organize when prompted

## How it Works

The script sorts files into the following subfolders:
- Images → .jpg, .jpeg, .png
- Videos → .mp4, .mov, .avi
- Documents → .pdf, .docx, .txt
- Music → .mp3, .wav
- Other → anything else
## Example

Before:
Downloads/
photo.jpg
report.pdf
song.mp3
movie.mp4

After:
Downloads/
Images/photo.jpg
Documents/report.pdf
Music/song.mp3
Videos/movie.mp4
