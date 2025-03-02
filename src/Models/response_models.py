from pydantic import BaseModel


# OpenAI API
class OpenAI_Post(BaseModel):
    title: str
    content: str
    image: str
    tags: list[str]


# Application API
class limited_json(BaseModel):
    id: str
    title: str
    content: str
    image: str
    tags: list[str]

    class Config:
        json_encoders = {str: lambda v: v[:20] if len(v) > 20 else v}


# POST API


class BoolListRequest(BaseModel):
    bool_list: list[bool]


class JsonResponse(BaseModel):
    id: str
    title: str
    content: str
    image: str
    tags: list[str]
