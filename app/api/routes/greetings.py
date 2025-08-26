"""Greeting API endpoints."""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
import random
from datetime import datetime


router = APIRouter(tags=["Greetings"])


# Response models
class GreetingResponse(BaseModel):
    """Greeting response model."""
    message: str
    timestamp: str
    vibe_level: str
    emoji: str


class PersonalizedGreetingResponse(BaseModel):
    """Personalized greeting response model."""
    message: str
    name: str
    timestamp: str
    vibe_level: str
    emoji: str
    fun_fact: str


# Vibe data
VIBE_LEVELS = ["🌟 Amazing", "✨ Fantastic", "🎵 Groovy", "🚀 Epic", "💫 Stellar", "🎉 Wonderful"]
EMOJIS = ["😊", "🎉", "✨", "🌟", "🎵", "🚀", "💫", "🎊", "🌈", "🎯"]
FUN_FACTS = [
    "Did you know? Python was named after Monty Python's Flying Circus!",
    "Fun fact: The first computer bug was an actual bug - a moth trapped in a Harvard computer in 1947!",
    "Amazing fact: There are more possible games of chess than atoms in the observable universe!",
    "Cool fact: The term 'debugging' was coined by Grace Hopper in the 1940s!",
    "Interesting fact: JavaScript was created in just 10 days in 1995!",
    "Did you know? The '@' symbol was used in email addresses for the first time in 1971!"
]


@router.get("/hello", response_model=GreetingResponse)
async def hello_world():
    """Simple Hello World endpoint with good vibes! ✨
    
    Returns a cheerful greeting with timestamp and random vibe elements.
    """
    return GreetingResponse(
        message="Hello World! Welcome to Vibe Coding Extended! 🎉",
        timestamp=datetime.now().isoformat(),
        vibe_level=random.choice(VIBE_LEVELS),
        emoji=random.choice(EMOJIS)
    )


@router.get("/hello/{name}", response_model=PersonalizedGreetingResponse)
async def hello_personalized(
    name: str,
    vibe: Optional[str] = Query(None, description="Custom vibe level")
):
    """Personalized greeting endpoint.
    
    Args:
        name: Name of the person to greet
        vibe: Optional custom vibe level
    
    Returns:
        Personalized greeting with fun facts and vibe energy!
    """
    if len(name) > 50:
        raise HTTPException(status_code=400, detail="Name too long! Keep it under 50 characters.")
    
    if not name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty!")
    
    # Clean the name
    clean_name = name.strip().title()
    
    return PersonalizedGreetingResponse(
        message=f"Hello {clean_name}! Ready to code with amazing vibes?",
        name=clean_name,
        timestamp=datetime.now().isoformat(),
        vibe_level=vibe if vibe else random.choice(VIBE_LEVELS),
        emoji=random.choice(EMOJIS),
        fun_fact=random.choice(FUN_FACTS)
    )


@router.get("/greetings/random", response_model=GreetingResponse)
async def random_greeting():
    """Get a random motivational greeting.
    
    Returns a random inspirational message perfect for coding sessions!
    """
    messages = [
        "Time to create something amazing! 🚀",
        "Let's code with passion and purpose! ✨",
        "Every line of code is a step toward greatness! 🌟",
        "Ready to turn caffeine into code? ☕💻",
        "Debug like a detective, code like an artist! 🎨",
        "The only way to do great work is to love what you do! 💝",
        "Code is poetry written in logic! 📝✨",
        "Think twice, code once, celebrate always! 🎉"
    ]
    
    return GreetingResponse(
        message=random.choice(messages),
        timestamp=datetime.now().isoformat(),
        vibe_level=random.choice(VIBE_LEVELS),
        emoji=random.choice(EMOJIS)
    )


@router.get("/greetings/stats")
async def greeting_stats():
    """Get statistics about available greetings.
    
    Returns metadata about the greeting system.
    """
    return {
        "total_vibe_levels": len(VIBE_LEVELS),
        "total_emojis": len(EMOJIS),
        "total_fun_facts": len(FUN_FACTS),
        "available_endpoints": [
            "/hello",
            "/hello/{name}",
            "/greetings/random",
            "/greetings/stats"
        ],
        "vibe_energy": "Maximum! 🔥"
    }