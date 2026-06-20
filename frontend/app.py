import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    layout="wide"
)

st.title("🤖 Enterprise RAG Assistant")
st.write("Upload a PDF and ask questions about it.")

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

if "chat" not in st.session_state:
    st.session_state.chat = []

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    if st.button("Upload & Index PDF"):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        with st.spinner("Uploading and indexing PDF..."):
            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

        if response.status_code == 200:
            st.session_state.uploaded = True
            st.success("PDF uploaded and indexed successfully!")
        else:
            st.error("Upload failed.")

st.divider()

question = st.text_input(
    "Ask a question about your documents"
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            response = requests.post(
                f"{API_URL}/ask",
                json={
                    "question": question
                }
            )

        result = response.json()

        st.session_state.chat.append(result)

for item in st.session_state.chat:
    st.subheader("Question")
    st.write(item["question"])

    st.subheader("Answer")
    st.write(item["answer"])

    st.subheader("Sources")
    for source in item["sources"]:
        st.write(
            f"📄 {source['source']} | Chunk {source['chunk_id']}"
        )

    st.divider()