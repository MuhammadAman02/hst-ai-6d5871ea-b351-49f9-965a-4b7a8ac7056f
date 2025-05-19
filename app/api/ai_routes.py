from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
import logging

from app.models.ai_models import (
    Message, Conversation,
    MedicalQuery, MedicalResponse
)
from app.services.ai_services import MedicalChatbotService

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Service dependencies
def get_medical_chatbot_service():
    """Dependency for medical chatbot service."""
    return MedicalChatbotService(model_name="medical-gpt")

# Medical Chatbot endpoint
@router.post("/medical-chat", response_model=MedicalResponse)
async def medical_chat(
    query: MedicalQuery,
    medical_service: MedicalChatbotService = Depends(get_medical_chatbot_service)
):
    """Medical chatbot endpoint for health-related queries."""
    try:
        return await medical_service.generate_response(query)
    except Exception as e:
        logger.error(f"Error in medical chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Keep other endpoints (chat, analyze, recommend, detect-fraud) as they were...