# 🚀 rag-client-local

> **A fully local Retrieval-Augmented Generation (RAG) client that lets you ask questions over lecture videos and get answers grounded to exact lecture numbers and timestamps — powered entirely by open-source models.**

---

## 📌 Motivation

When learning from long video lectures, it’s difficult to remember **which lecture** and **which exact timestamp** explains a particular concept.

This project solves that problem by:
- Converting lecture videos into searchable knowledge
- Using **local embeddings + local LLMs**
- Returning **context-aware answers with precise lecture and time references**
- Running **100% locally** — no cloud APIs, no data leakage

---

## 🧠 What This Project Does

`rag-client-local` builds a **local RAG pipeline** over video lectures:

1. Extracts audio from lecture videos
2. Converts speech → text using a local Whisper model
3. Chunks transcripts with timestamps
4. Generates embeddings locally
5. Retrieves the most relevant chunks for a user query
6. Feeds them to a local LLM for grounded answer generation

---

## 🏗️ Architecture / Workflow

```
Lecture Videos
      ↓
FFmpeg (Audio Extraction)
      ↓
Whisper (Speech → Text)
      ↓
Timestamped Text Chunks
      ↓
Local Embeddings (bge-m3)
      ↓
Cosine Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
LLM Prompt (llama3.2)
      ↓
Final Answer + Lecture References
```

---

## ⚙️ Tech Stack

- **Language:** Python
- **Audio Processing:** FFmpeg (via `subprocess`)
- **Speech-to-Text:** OpenAI Whisper (local, `medium` model)
- **Embeddings:** `bge-m3` via Ollama
- **Vector Storage:** Pandas DataFrame (persisted with `joblib`)
- **Similarity Search:** Cosine similarity
- **LLM:** `llama3.2` (local, via Ollama)
- **APIs:** Ollama HTTP API

---

## ✨ Key Features

- **Fully local pipeline** (no cloud dependency)
- Converts **lecture videos → searchable text**
- **Timestamp-aware chunks** (start & end times preserved)
- Efficient reuse using **precomputed embeddings**
- Semantic search using **cosine similarity**
- LLM answers grounded strictly in retrieved context
- Outputs **lecture number + timestamp**, not hallucinated answers

---

## 🛠️ Installation & Setup

```bash
git clone https://github.com/teradadcodez/rag-client-local.git
cd rag-client-local
pip install -r requirements.txt
ollama serve
ollama pull bge-m3
ollama pull llama3.2
```

Ensure `ffmpeg` is installed and available in PATH.

---

## 🚀 Usage

1. Extract audio from lectures
2. Transcribe using Whisper
3. Create timestamped chunks
4. Generate embeddings and persist them
5. Ask questions using semantic search + LLM

---

## 📊 Future Improvements

- Replace DataFrame with FAISS / Qdrant
- Add Web UI
- Clickable timestamps
- Streaming responses
- Docker support

---

## 👨‍💻 Author

**Tanmay Jain**  
GitHub: https://github.com/teradadcodez

---

## 🙏 Credits & Acknowledgements

- **CodeWithHarry** – Inspiration and conceptual guidance for Python, AI, and system design concepts used in this project.  
  YouTube: https://www.youtube.com/@CodeWithHarry  
  GitHub: https://github.com/CodeWithHarry