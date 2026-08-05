# 🤖 AI Resume Analyzer using RAG

An AI-powered Resume Analyzer built using FastAPI, LangChain, FAISS, Sentence Transformers, Ollama (Llama 3.2), Streamlit, and Docker.

## 🚀 Features

- Upload Resume (PDF)
- AI-powered Resume Analysis
- Retrieval-Augmented Generation (RAG)
- FastAPI REST API
- Streamlit User Interface
- Dockerized Deployment

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Ollama (Llama 3.2)
- Docker
- Git & GitHub

## 📂 Project Structure

```text
ResumeAnalyzer/
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   └── llm.py
│
├── frontend/
│   └── app.py
│
├── uploads/
├── vector_store/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ Run Locally

```bash
docker compose up --build
```

Backend

http://localhost:8000

Frontend

http://localhost:8501

## Future Improvements

- Resume ATS Score
- Skill Gap Analysis
- Job Recommendation
- Cloud Deployment (Azure / Render / AWS)
