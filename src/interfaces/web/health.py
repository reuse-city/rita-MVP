# src/interfaces/web/health.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    ollama_status: str
    version: str = "0.1.0"

@router.get("/health", response_model=HealthResponse)
async def health_check():
    try:
        # Check Ollama
        ollama_response = requests.get("http://localhost:11434/api/tags")
        ollama_status = "healthy" if ollama_response.status_code == 200 else "unhealthy"
        
        return HealthResponse(
            status="healthy",
            ollama_status=ollama_status
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))