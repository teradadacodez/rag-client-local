import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list) : 
    req = requests.post("http://localhost:11434/api/embed",
                        json={"model":"bge-m3",
                              "input":text_list})
    embeddings = req.json()["embeddings"]
    return embeddings

# a = create_embedding(["tanmay jain is a good boy","tanmay jain lives in alwar"])
# print(a[0],"\n\n\n\n",a[1])
# print(type(a),type(a[0]),type(a[1]))


jsons = os.listdir("chunks/") # listed all the jsons !
my_dicts = []
chunk_id = 0

for json_file in jsons :
    file = None
    with open(f"chunks/{json_file}","r",encoding="utf-8") as f:
        file = json.load(f)
    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c["text"] for c in file["chunks"]])

    for i,chunk in enumerate(file["chunks"]) : 
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)


df = pd.DataFrame.from_records(my_dicts)
# save this dataframe 
joblib.dump(df,"embeddings.joblib")