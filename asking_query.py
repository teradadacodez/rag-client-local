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

def inference(prompt) :
    r = requests.post("http://localhost:11434/api/generate",\
                      json={"model":"llama3.2",
                            "prompt":prompt,
                            "stream":False})
    response = r.json()
    return response

df = joblib.load("embeddings.joblib")
query = input("Ask a Question : ")
query_embedding = create_embedding([query])[0]


# finding similarities of query_embedding with chunk_embeddings
similarities = cosine_similarity(np.vstack(df["embedding"]),[query_embedding]).flatten()
# print(similarities)

top_results = 50
top_chunk_indices = similarities.argsort()[::-1][0:top_results]

new_df = df.loc[top_chunk_indices]
# print(new_df[["number","text"]])

prompt = f"""Here are video subtitle chunks containing video number, the start time in seconds, 
the end time in seconds
and the text at that time:
{new_df[["number","start","end","text"]].to_json(orient="records")}--------------------
"{query}"
User has asked this question related to the video subtitle chunks, 
you have to answer in human way that where and how much content is taught
in which video and at what timestamp and guide the user to go to that particular video.
if asked question is unrelated to the course then tell the user that only related questions can be answered.
"""

with open("prompt.txt","w") as f :
    f.write(prompt)

response = inference(prompt)["response"]

with open("response.txt","w") as f :
    f.write(response)