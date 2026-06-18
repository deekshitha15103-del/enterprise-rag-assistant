from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Assistant",
    description="AWS Bedrock + Claude + RAG System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Enterprise RAG Assistant is running successfully!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }