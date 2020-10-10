import sys
from dotenv import load_dotenv, find_dotenv

sys.path.insert(0, '..')
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

import orjson

from fastapi import FastAPI
from pydantic import BaseModel, typing
from starlette.responses import JSONResponse
import uvicorn
from bot import Chatbot


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
    print(Chatbot.perguntar(pergunta))

    return {'resposta': ' kk! sla,vey'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
# https://github.com/aibox-redacao/arquitetura-api-correcao/tree/218a03703ef89ae91be954be4164ede0f0067a96/corretor
