"""Custom middleware for the FastAPI application."""

import time
from fastapi import Request, Response


async def add_process_time_header(request: Request, call_next):
    """Add process time header to all responses.
    
    This middleware calculates the time taken to process each request
    and adds it to the response headers.
    """
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f"{process_time:.4f}")
    response.headers["X-Powered-By"] = "Vibe-Coding-Extended ✨"
    return response