from fastapi import FastAPI
from models.request_model import MyRequestModel

app = FastAPI()
@app.post("/predict")
async def predict(data: MyRequestModel):
    # Dummy model logic
    result = {"message": f"Hello {data.name}, you are {date.age} years old."}
    return result