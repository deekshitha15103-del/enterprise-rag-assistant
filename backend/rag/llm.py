from backend.llm.claude_client import ClaudeClient

client = ClaudeClient()

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a strict RAG assistant.

Rules:
- Answer ONLY using the context below
- If answer is not in context, say "I don't know"
- Do NOT guess
- Be clear and concise

Context:
{context}

Question:
{query}

Answer:
"""

    return client.invoke(prompt)