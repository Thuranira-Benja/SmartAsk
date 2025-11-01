from fastapi import APIRouter
from pydantic import BaseModel
from .qa_flow import check_hardcoded
from .rag_service import build_or_get_vectordb, answer_with_rag
from .docs_loader import load_demo_documents

router = APIRouter()

class ChatPayload(BaseModel):
    question: str

documents = load_demo_documents()
vectordb = build_or_get_vectordb(documents)

@router.post("/chat")
async def chat(payload: ChatPayload):
    q = payload.question
    hard = check_hardcoded(q)
    if hard:
        return {"answer": hard, "source": "hardcoded"}
    answer = answer_with_rag(q, vectordb)
    return {"answer": answer, "source": "rag"}
