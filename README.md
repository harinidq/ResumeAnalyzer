# 🤖 AI Resume Analyzer using RAG

An AI-powered Resume Analyzer that analyzes PDF resumes using **Retrieval-Augmented Generation (RAG)** and Large Language Models (LLMs). The application provides AI-generated feedback on resumes through an interactive web interface and REST API.

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 🤖 AI-powered Resume Analysis
- 🔍 Retrieval-Augmented Generation (RAG)
- 🧠 Sentence Transformer Embeddings
- 📚 FAISS Vector Database
- 🌐 FastAPI REST API
- 💻 Streamlit Web Interface
- 🐳 Dockerized Deployment

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM | Ollama (Llama 3.2) |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | Sentence Transformers |
| PDF Processing | PyPDF |
| Deployment | Docker |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
ResumeAnalyzer/
│
├── backend/
│   ├── llm.py
│   ├── main.py
│   └── rag.py
│
├── frontend/
│   └── app.py
│
├── uploads/
├── vector_store/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/harinidq/ResumeAnalyzer.git
cd ResumeAnalyzer
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Start FastAPI

```bash
uvicorn backend.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger API:

```
http://localhost:8000/docs
```

---

### Start Streamlit

```bash
streamlit run frontend/app.py
```

Frontend:

```
http://localhost:8501
```

---

## 🐳 Docker

Build Docker Image

```bash
docker build -t resumeanalyzer .
```

Run Container

```bash
docker run -p 8000:8000 resumeanalyzer
```

---

## 📸 Demo

### Streamlit Interface

<img width="1917" height="1011" alt="image" src="https://github.com/user-attachments/assets/315a65c2-f008-4a0c-b996-3cb1c85584e1" />
<img width="1917" height="1000" alt="image" src="https://github.com/user-attachments/assets/f9f0e225-a552-4aa5-9532-d9fb510f4a23" />



### FastAPI Swagger

<img width="1903" height="850" alt="image" src="https://github.com/user-attachments/assets/ca483505-c27e-4cf4-9621-109ae5827e7d" />


### Docker Container

<img width="1337" height="107" alt="image" src="https://github.com/user-attachments/assets/03c1dc0a-9ea6-4563-994e-31259ffd8ca6" />


---

## 🔄 Workflow

```text
Resume PDF
      │
      ▼
PyPDF Loader
      │
      ▼
Text Splitting
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Relevant Context Retrieval
      │
      ▼
Llama 3.2 (Ollama)
      │
      ▼
AI Resume Analysis
      │
      ▼
Streamlit UI
```

---

## 🚀 Future Improvements

- ATS Resume Score
- Job Recommendation System
- Skill Gap Analysis
- Resume Improvement Suggestions
- Cloud Deployment (AWS / Azure / Render)
- Authentication & User Login

---

## 👩‍💻 Author

**Harini M D**

- GitHub: https://github.com/harinidq
- LinkedIn: https://www.linkedin.com/in/harini-md-745a17263/

---
