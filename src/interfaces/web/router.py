# src/interfaces/web/router.py
from fastapi import APIRouter, HTTPException
from models.chat import ChatRequest, ChatResponse
from core.chat.engine import ChatEngine
from core.logging import get_logger

router = APIRouter()
logger = get_logger("rita.chat")

# Will be set during application startup
chat_engine: ChatEngine = None

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not chat_engine:
        logger.error("Chat endpoint called before chat engine initialization")
        raise HTTPException(500, "Chat engine not initialized")
    
    try:
        logger.info("Processing chat request")
        logger.debug(f"Chat request message: {request.message}")
        logger.debug(f"Chat context: {request.context}")
        
        response, context = await chat_engine.process_message(
            message=request.message,
            context=request.context
        )
        
        logger.info("Chat request processed successfully")
        logger.debug(f"Chat response: {response}")
        logger.debug(f"Updated context: {context}")
        
        return ChatResponse(response=response, context=context)
        
    except Exception as e:
        error_msg = f"Chat error: {str(e)}"
        logger.exception(error_msg)
        raise HTTPException(500, error_msg)
