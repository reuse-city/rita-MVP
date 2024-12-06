# src/services/llm/ollama_service.py
import requests
from typing import Dict, List, Optional
from .base import BaseLLMService

class OllamaService(BaseLLMService):
    """Implementation of LLM service using Ollama."""
    
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama2"):
        self.base_url = base_url
        self.model = model
        self.api_url = f"{base_url}/api/generate"
    
    async def initialize(self) -> None:
        """Check if Ollama is running and the model is available."""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            if response.status_code != 200:
                raise ConnectionError("Ollama server is not responding")
            # Check if our model is available
            if self.model not in str(response.json()):
                raise ValueError(f"Model {self.model} is not available in Ollama")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to Ollama: {e}")
    
    async def generate_response(
        self,
        prompt: str,
        context: Optional[List[Dict[str, str]]] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """Generate a response using Ollama."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt if system_prompt else "",
            "context": context if context else []
        }
        
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to generate response: {e}")
    
    async def health_check(self) -> bool:
        """Check if Ollama service is healthy."""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False