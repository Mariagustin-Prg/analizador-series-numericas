from fastapi import FastAPI
from backend.funciones_numericas import MCD_iterable, media, sigma, primos_en_lista
from models.body import Body

app = FastAPI()

# Raíz
app.get("/")
async def root():
    return {"message": "API de Análisis de Series Numéricas",
            "github": "https://github.com/Mariagustin-Prg/analizador-series-numericas"}


#Maximo Común Divisor
@app.get("/mcd", response_model= dict)
async def calcular_maximo_comun_divisor(body: Body):
    response = {
        "Máximo común Divisor": MCD_iterable(body.serie)
        }
        
    return response

# Media y Desviación Estándar
@app.get("/media_desviacion", response_model= dict)
async def calcular_media_y_desviacion(body: Body):
    response = {
        "Media": media(body.serie),
        "Desviacion": sigma(body.serie)
    }
    return response

# Primalidad de números en una lista
@app.get("/primalidad", response_model= dict)
async def verificar_primalidad_en_lista(body: Body):
    response = {
        "Primos en la lista": primos_en_lista(body.serie)
    }
    return response