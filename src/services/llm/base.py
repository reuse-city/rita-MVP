# src/services/llm/base.py
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class BaseLLMService(ABC):
    """Base class for LLM services."""
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the LLM service."""
        pass
    
    @abstractmethod
    async def generate_response(
        self,
        prompt: str,
        context: Optional[List[Dict[str, str]]] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """Generate a response from the LLM."""
        pass
    
    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the LLM service is healthy and responding."""
        pass