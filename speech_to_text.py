import whisper
import os
import datetime as dt
import json

a = dt.datetime.now()

audio_files = os.listdir()

model = whisper.load_model("medium")

i = 1 
for file in audio_files :
    audio_path = f"audios/audio ({i}).mp3"

    print(f"Transcribing : audio ({i}).mp3")

    json_path = f"texts/output{i}.json"
    
    result = model.transcribe(audio=audio_path,
                              language="en",
                              task="transcribe")
    with open(json_path,"w",encoding="utf-8") as f :
        json.dump(result,f)
    print(f"saved : {json_path.split("/")[1]}")
    i+=1        

b = dt.datetime.now()

print(b-a)


