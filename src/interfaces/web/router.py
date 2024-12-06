# src/interfaces/web/router.py
from fastapi import APIRouter, HTTPException
from src.models.chat import ChatRequest, ChatResponse
from src.core.chat.engine import ChatEngine

router = APIRouter()

# Will be set during application startup
chat_engine: ChatEngine = None

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response, context = await chat_engine.process_message(
            message=request.message,
            context=request.context
        )
        return ChatResponse(response=response, context=context)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))