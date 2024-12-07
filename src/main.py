# src/main.py
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from services.llm.ollama_service import OllamaService
from core.chat.engine import ChatEngine
from interfaces.web.router import router
from interfaces.web import router as web_router
from core.logging import setup_logging, get_logger
from config import Config

# Load configuration
config = Config.load()

# Initialize logging
logger = setup_logging()
app_logger = get_logger("rita.app")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app_logger.info("Initializing RITA services")
    # Initialize LLM service
    llm_service = OllamaService(
        base_url=config.llm.base_url,
        model=config.llm.model
    )
    await llm_service.initialize()
    
    # Initialize chat engine
    web_router.chat_engine = ChatEngine(llm_service)
    
    app_logger.info("RITA services initialized")
    yield
    app_logger.info("Shutting down RITA services")
    await llm_service.cleanup()  # Clean up resources

app = FastAPI(
    title=config.app.name,
    lifespan=lifespan
)

# Add root route
@app.get("/")
async def root():
    return {
        "name": config.app.name,
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    app_logger.info("Health check requested")
    return {"status": "healthy"}

# Register routes
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.app.host,
        port=config.app.port,
        reload=config.app.debug
    )
