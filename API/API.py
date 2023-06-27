class API:
    @classmethod
    def reversa(cls,frase:str)->str:
        frase={
            'clave':frase
        }
        contenido=frase['clave']
        contenido_reversa=contenido[::-1]
        return contenido_reversa