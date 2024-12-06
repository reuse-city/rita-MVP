# src/models/chat.py
from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str  # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    message: str
    context: Optional[List[ChatMessage]] = None

class ChatResponse(BaseModel):
    response: str
    context: List[ChatMessage]