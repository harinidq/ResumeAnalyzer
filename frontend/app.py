import streamlit as st
import requests

API = "http://127.0.0.1:8000/chat"

st.title("🤖 AI Resume Chatbot")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    if uploaded_file is None:

        st.warning("Upload a PDF first.")

    elif question == "":

        st.warning("Enter a question.")

    else:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        data = {
            "question": question
        }

        response = requests.post(
            API,
            files=files,
            data=data
        )

        if response.status_code == 200:

            st.success("Answer")

            st.write(
                response.json()["answer"]
            )

        else:

            st.error(response.text)