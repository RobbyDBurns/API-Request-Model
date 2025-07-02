from pydantic import BaseModel

class MyRequestModel(BaseModel):
    name: str
    age: int