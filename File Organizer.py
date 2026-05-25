import os
import shutil

folder_path = input("What folder path would you like to organize (Ex: C:/Users/JohnS/Downloads)? ")
files = os.listdir(folder_path)

for file in files: 
    full_path = os.path.join(folder_path, file) 
    if os.path.isfile(full_path):                     
        extension = os.path.splitext(file)[1]        

        if extension in [".jpg", ".jpeg", ".png"]:
            folder = "Images"
        elif extension in [".mp4", ".mov", ".avi"]:
            folder = "Videos"
        elif extension in [".pdf", ".docx", ".txt"]:
            folder = "Documents"
        elif extension in [".mp3", ".wav"]:
            folder = "Music"
        else:
            folder = "Other"

        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
        shutil.move(full_path, os.path.join(folder_path, folder, file))