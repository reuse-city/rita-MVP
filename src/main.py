# src/main.py
import os
import uvicorn
from fastapi import FastAPI
from src.services.llm.ollama_service import OllamaService
from src.core.chat.engine import ChatEngine
from src.interfaces.web.router import router
from src.interfaces.web import router as web_router
from src.config import Config

# Load configuration based on environment
env = os.getenv('RITA_ENV', 'development')
config = Config.load(env)

app = FastAPI(title=config.app.name)

@app.on_event("startup")
async def startup_event():
    # Initialize LLM service with config
    llm_service = OllamaService(
        base_url=config.llm.base_url,
        model=config.llm.model
    )
    await llm_service.initialize()
    
    # Initialize chat engine
    web_router.chat_engine = ChatEngine(llm_service)

# Register routes
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.app.host,
        port=config.app.port,
        reload=config.app.debug
    )