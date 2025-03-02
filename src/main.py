"""
Main program of FastAPI application.
"""

from fastapi import FastAPI
from Services.openai_service import openai_agent
from Models.response_models import limited_json

app = FastAPI()


@app.get("/")
async def root():
    response = openai_agent.process_news("art")
    return response
