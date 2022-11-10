class Propiedad:
    def __init__(self,barrio:str,tipo:str,precio:float,ambientes:int,propietario:int) -> None:
        self.barrio = barrio    #barrio donde esta ubicada la propierdad   
        self.tipo = tipo    #tipo de propiedad
        self.precio = precio    
        self.ambientes = ambientes
        self.propietario = propietario
        self.disponibilidad = "Disponible"


    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.precio<other.precio
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.precio<=other.precio
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.precio==other.precio
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.precio!=other.precio
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.precio>other.title
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.precio>=other.precio
    
        
    def __str__(self) -> str:
        return f"Barrio: {self.barrio}\nTipo: {self.tipo}\nAmbientes: {self.ambientes}\nPrecio: {self.precio}"