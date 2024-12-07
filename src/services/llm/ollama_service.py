# src/services/llm/ollama_service.py
import os
import time
from typing import Dict, List, Optional
import httpx
from .base import BaseLLMService

class OllamaService(BaseLLMService):
    def __init__(self, base_url: str = "http://ollama:11434", model: str = "llama2"):
        self.base_url = os.getenv("OLLAMA_HOST", base_url)
        self.model = model
        self.api_url = f"{self.base_url}/api/generate"
        self.max_retries = 5
        self.retry_delay = 10  # seconds
        self.client = httpx.AsyncClient(timeout=60.0)

    async def initialize(self) -> None:
        """Check if Ollama is running and the model is available."""
        for attempt in range(self.max_retries):
            try:
                response = await self.client.get(f"{self.base_url}/api/tags")
                if response.status_code != 200:
                    raise ConnectionError("Ollama server is not responding")
                
                if self.model not in str(response.json()):
                    if attempt < self.max_retries - 1:
                        print(f"Model {self.model} not found, retrying in {self.retry_delay} seconds...")
                        await asyncio.sleep(self.retry_delay)
                        continue
                    raise ValueError(f"Model {self.model} is not available in Ollama")
                return
            except httpx.RequestError as e:
                if attempt < self.max_retries - 1:
                    print(f"Failed to connect to Ollama, retrying in {self.retry_delay} seconds...")
                    await asyncio.sleep(self.retry_delay)
                    continue
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
            response = await self.client.post(self.api_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except httpx.RequestError as e:
            raise ConnectionError(f"Failed to generate response: {e}")

    async def health_check(self) -> bool:
        """Check if Ollama service is healthy."""
        try:
            response = await self.client.get(f"{self.base_url}/api/tags")
            return response.status_code == 200 and self.model in str(response.json())
        except httpx.RequestError:
            return False

    async def cleanup(self):
        """Cleanup resources."""
        await self.client.aclose()
