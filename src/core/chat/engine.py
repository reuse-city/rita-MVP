# src/core/chat/engine.py
from typing import List, Optional
from src.models.chat import ChatMessage
from src.services.llm.base import BaseLLMService

class ChatEngine:
    def __init__(self, llm_service: BaseLLMService):
        self.llm_service = llm_service
        self.system_prompt = """You are RITA, an AI assistant specialized in helping people repair and maintain physical objects. 
        You are knowledgeable about repair techniques, tools, and safety considerations. 
        Always prioritize safety in your advice and warn users about potential risks. 
        If you're unsure about something, admit it and suggest consulting a professional."""
    
    async def process_message(
        self,
        message: str,
        context: Optional[List[ChatMessage]] = None
    ) -> tuple[str, List[ChatMessage]]:
        # Convert context to format expected by LLM
        llm_context = []
        if context:
            llm_context = [{"role": msg.role, "content": msg.content} for msg in context]
        
        # Generate response
        response = await self.llm_service.generate_response(
            prompt=message,
            context=llm_context,
            system_prompt=self.system_prompt
        )
        
        # Update context
        new_context = context or []
        new_context.extend([
            ChatMessage(role="user", content=message),
            ChatMessage(role="assistant", content=response)
        ])
        
        return response, new_context