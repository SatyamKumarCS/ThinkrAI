import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Add parent directory to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.engine import SocraticEngine

app = FastAPI(title="ThinkrAI API", description="Socratic DSA Tutor Backend")

# Allow CORS for Streamlit Cloud frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize engine on startup
engine = None

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@app.on_event("startup")
async def startup():
    global engine
    engine = SocraticEngine()
    print("SocraticEngine initialized successfully!")

@app.get("/")
async def root():
    return {"status": "ThinkrAI API is running"}

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    response = engine.query(request.question)
    return QueryResponse(answer=response)
