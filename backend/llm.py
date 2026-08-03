from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.3
)

def ask_llm(context, question):

    prompt = f"""
You are an AI Resume Assistant.

Answer ONLY using the resume information below.

Resume:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content