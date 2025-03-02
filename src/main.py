"""
Main program of FastAPI application.
"""

from fastapi import FastAPI
from Services.openai_service import openai_agent
from Services.solr_service import solr_agent
from Models.response_models import limited_json, BoolListRequest, JsonResponse

app = FastAPI()


@app.get("/")
async def root():
    response = openai_agent.check_status()
    return {"message": response}


@app.post("/post")
async def post_post(request: BoolListRequest):
    return {"message": "Hello"}


@app.get("/get")
async def get_post():
    return solr_agent.random_post()
