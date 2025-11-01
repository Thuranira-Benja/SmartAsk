from fastapi import FastAPI
from .api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartAsk — RAG Chat Assistant")
app.include_router(router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "SmartAsk backend running"}
