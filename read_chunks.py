import requests
import os
import json

def create_embedding(text) : 
    req = requests.post("http://localhost:11434/api/embeddings",
                        json={"model":"bge-m3","prompt":text})

    embedding = req.json()["embedding"]

    return embedding

jsons = os.listdir("chunks/")
print(jsons)

my_dicts = []
chunk_id = 0
for json_file in jsons :
    file = None
    with open(f"chunks/{json_file}","r",encoding="utf-8") as f:
        file = json.load(f)
    for chunk in file["chunks"] : 
        chunk['chunk_id'] = chunk_id
        chunk_embedding = create_embedding(chunk["text"])
        chunk_id += 1
        my_dicts.append(chunk)
        print(chunk)
    break 

print(my_dicts)