import requests


def create_embedding(text) : 
    req = requests.post("http://localhost:11434/api/embeddings",
                        json={"model":"bge-m3","prompt":text})

    embedding = req.json()["embedding"]

    return embedding


temp = create_embedding("cat sat on the mat")
print(temp)