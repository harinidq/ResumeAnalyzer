from fastapi import FastAPI, UploadFile, File, Form

from backend.rag import chatbot

app = FastAPI(
    title="AI Resume Chatbot"
)

@app.get("/")
def home():

    return {
        "message": "AI Resume Chatbot API Running"
    }


@app.post("/chat")

async def chat(
    file: UploadFile = File(...),
    question: str = Form(...)
):

    pdf = await file.read()

    answer = chatbot(
        pdf,
        question
    )

    return {
        "answer": answer
    }