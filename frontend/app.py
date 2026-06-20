import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

if "chat" not in st.session_state:
    st.session_state.chat = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

with st.sidebar:
    st.title("📚 Knowledge Base")

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

            with st.spinner("Indexing document..."):
                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

            if response.status_code == 200:
                st.session_state.uploaded_files.append(uploaded_file.name)
                st.success("PDF indexed successfully!")
            else:
                st.error("Upload failed. Check backend.")

    st.divider()

    st.subheader("Uploaded Files")

    if st.session_state.uploaded_files:
        for file_name in st.session_state.uploaded_files:
            st.write(f"📄 {file_name}")
    else:
        st.caption("No files uploaded in this session.")

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.chat = []
        requests.delete(f"{API_URL}/history")
        st.success("Chat cleared.")


st.title("🤖 Enterprise RAG Assistant")
st.caption("Ask questions from your PDFs using FAISS retrieval + Llama 3.2.")

for message in st.session_state.chat:
    with st.chat_message("user"):
        st.write(message["question"])

    with st.chat_message("assistant"):
        st.write(message["answer"])

        with st.expander("Sources"):
            for source in message["sources"]:
                st.write(
                    f"📄 **{source['source']}** | Chunk `{source['chunk_id']}`"
                )
                st.caption(source["preview"])


question = st.chat_input("Ask a question about your uploaded documents...")

if question:
    with st.chat_message("user"):
        st.write(question)

    with st.spinner("Thinking..."):
        response = requests.post(
            f"{API_URL}/ask",
            json={
                "question": question
            }
        )

    result = response.json()

    st.session_state.chat.append(result)

    with st.chat_message("assistant"):
        st.write(result["answer"])

        with st.expander("Sources"):
            for source in result["sources"]:
                st.write(
                    f"📄 **{source['source']}** | Chunk `{source['chunk_id']}`"
                )
                st.caption(source["preview"])