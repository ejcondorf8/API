from API.API import API
from pydantic import BaseModel

class Documents(BaseModel):
    string:str=''

def devolver():
    contenido=API.reversa(
        frase='HOLA MUNDO'
    )
    return contenido