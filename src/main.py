from config import *

import orjson

from fastapi import FastAPI
from pydantic import BaseModel, typing
from starlette.responses import JSONResponse
import uvicorn


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)


app = FastAPI(default_response_class=ORJSONResponse)


# pydantic models


class StockIn(BaseModel):
    pergunta: str


class StockOut(BaseModel):
    resposta: str


# routes


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.post("/responde", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    pergunta = payload.pergunta
    print(pergunta)
    return {'resposta': ' kk! sla,vey'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
