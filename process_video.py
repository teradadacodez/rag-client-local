# this program is to convert videos to mp3 files !
import os
import subprocess
files = os.listdir("Lectures")

for file in files :
    tutnum = file.split(" ")[-1].split(".")[0].split("(")[1].split(")")[0]
    file_name = file.split(".")
    print(file_name)
    print(tutnum)
    # subprocess.run(["ffmpeg","-i",f"Lectures/{file}", f"audios/{tutnum}_{file_name}.mp3"])
