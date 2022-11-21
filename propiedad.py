class Propiedad:
    def __init__(self, barrio:str, tipo:str, precio:float, ambientes:int, propietario:int,id:int) -> None:
        self.barrio = barrio    #barrio donde esta ubicada la propierdad   
        self.tipo = tipo    #tipo de propiedad
        self.precio = precio
        self.ambientes = ambientes
        self.propietario = propietario
        self.disponibilidad = "Disponible"
        self.id = id

    def __str__(self) -> str:
        return f" >> Barrio: {self.barrio}\n >> Tipo: {self.tipo}\n >> Ambientes: {self.ambientes}\n >> Precio: {self.precio}\n"
    
    def __eq__(self, other) -> bool:
        return self.id == other.id
    """
    def __lt__(self, other:float): # x<y llama x.__lt__(y)
        return self.precio<other.precio
    def __le__(self, other:float): # x<=y llama x.__le__(y)
        return self.precio<=other.precio
    def __eq__(self, other:float): # x==y llama x.__eq__(y)
        return self.precio==other.precio
    def __ne__(self, other:float): # x!=y llama x.__ne__(y)
        return self.precio!=other.precio
    def __gt__(self, other:float): # x>y llama x.__gt__(y)
        return self.precio>other.title
    def __ge__(self, other:float): # x>=y llama x.__ge__(y)
        return self.precio>=other.precio"""