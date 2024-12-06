# tests/test_chat.py
import pytest
from src.core.chat.engine import ChatEngine
from src.models.chat import ChatMessage
from src.services.llm.ollama_service import OllamaService

@pytest.mark.asyncio
async def test_chat_engine():
    # Initialize services
    llm_service = OllamaService()
    await llm_service.initialize()
    
    # Create chat engine
    chat_engine = ChatEngine(llm_service)
    
    # Test basic conversation
    message = "How do I fix a leaking faucet?"
    response, context = await chat_engine.process_message(message)
    
    # Basic assertions
    assert response is not None
    assert len(response) > 0
    assert len(context) == 2  # User message and assistant response
    assert context[0].role == "user"
    assert context[1].role == "assistant"