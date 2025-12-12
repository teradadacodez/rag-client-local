import json
import os 

text_files = os.listdir("texts/")

for file in text_files : 
    LecNo = file.split(".")[0][-1]
    result = None
    with open(f"texts/{file}","r",encoding="utf-8") as f :
        result = json.load(f)
    chunks = []
    for segment in result["segments"] : 
        chunks.append({"Lecture Number":f"Lecture : {LecNo}", "start":segment["start"], "end":segment["end"], "text":segment["text"]})
    chunks_with_metadata = {"chunks":chunks, "full_text":[result["text"]]}
    if(os.path.exists("chunks/")==False) :
        os.makedirs("chunks")
    with open(f"chunks/chunk_of_lecture{LecNo}.json","w",encoding="utf-8") as f :
        json.dump(chunks_with_metadata,f)

