This is my first RAG client project
In this project we are going to create a RAG bases LLM setup on which we can ask doubts by giving context to the LLM
Steps are :
1. Converting Videos to mp3 using ffmpeg (source = gyan.dev, for Win11 users ffmpeg/bin must be added to path)
2. Transcribing mp3 to a python dictionary (which is json-serializable) using openai-whisper-medium model
3. Extracting useful information from the json dump (calling it a 'chunk') for each file
4. Reading chunks and converting them into embeddings using ollama bge-m3 model
5. We will post request on 'http://localhost:11434/api/embeddings' and the pull the embeddings from there
6. We will now read chunks and extract only relevant info out of it! We'll put it into a pandas.DataFrame and dump that dataframe (using joblib) for future use
7. Now we will load the dataframe, ask user to ask a query/question, create embedding of that question, finding cosine similarity between question embedding and chunk embedding, finding top similarity score chunks, and feed the LLM a nicely written prompt in which we will pass the question and the top chunks
