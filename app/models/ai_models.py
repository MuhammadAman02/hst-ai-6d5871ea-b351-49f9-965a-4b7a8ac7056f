from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

class Message(BaseModel):
    """Represents a single message in a conversation."""
    content: str
    role: str = "user"  # "user" or "assistant"
    timestamp: datetime = Field(default_factory=datetime.now)

class Conversation(BaseModel):
    """Represents a conversation with multiple messages."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    messages: List[Message] = []
    metadata: Optional[Dict[str, Any]] = None

class MedicalQuery(BaseModel):
    """Represents a medical query from a user."""
    query: str
    user_age: Optional[int] = None
    user_gender: Optional[str] = None
    user_symptoms: Optional[List[str]] = None

class MedicalResponse(BaseModel):
    """Represents a response to a medical query."""
    answer: str
    disclaimer: str
    suggested_actions: List[str]
    confidence: float