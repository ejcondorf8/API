from fastapi import FastAPI
from test import Documents,devolver
app=FastAPI()

@app.post('/reversa')
def reversa(contenido:Documents):
    contenido=devolver()
    return{
        'frase':contenido
    }