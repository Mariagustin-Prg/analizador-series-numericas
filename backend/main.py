"""
main.py
FastAPI application entrypoint.
"""
from typing import Iterable
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.func_numericas import MCD, media, sigma, primalidad_lista

app = FastAPI()


class TwoInts(BaseModel):
    value_1: int
    value_2: int


class ListaNumeros(BaseModel):
    lista: Iterable[float]


@app.get("/")
async def root():
    return {"status": "ok", "message": "FastAPI backend running"}


@app.post("/maximo_comun_divisor")
async def endpoint_mcd(payload: TwoInts):
    try:
        result = MCD(payload.value_1, payload.value_2)
        return {"mcd": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/media_desviacion_estandar")
async def endpoint_media_sigma(payload: ListaNumeros):
    try:
        data = [float(k) for k in payload.lista]
        mean_val = media(data)
        std_val = sigma(data)
        return {"media": mean_val, "desviacion_estandar": std_val}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/primalidad_lista")
async def endpoint_primalidad_lista(payload: ListaNumeros):
    try:
        primes = primalidad_lista(list(payload.lista))
        return {"primos": primes}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


if __name__ == "__main__":
    pass
