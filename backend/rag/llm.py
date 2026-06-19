import ollama


def generate_answer(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context, say:
'I could not find that information in the uploaded documents.'
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]