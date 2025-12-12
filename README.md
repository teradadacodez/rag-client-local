This is my first RAG client project
In this project we are going to create a RAG bases LLM setup on which we can ask doubts by giving context to the LLM
Steps are :
1. Converting Videos to mp3 using ffmpeg (source = gyan.dev, for Win11 users ffmpeg/bin must be added to path
2. Transcribing mp3 to a python dictionary (which is json-serializable) using openai-whisper-medium model
3. Extracting useful information from the json dump (calling it a 'chunk') for each file
