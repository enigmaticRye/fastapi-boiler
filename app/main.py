from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.schemas import JSONResponseModel, UserOutModel


app = FastAPI()


@app.post("/validateResponse", response_model=UserOutModel)
async def root():
    resp = {"email": "mymail", "name": "myname"}
    return resp


