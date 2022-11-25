class Propiedad:
    def __init__(self, barrio:str, tipo:str, precio:int, ambientes:int, propietario:int, identificador:int) -> None:
        self.barrio = barrio    #barrio donde esta ubicada la propierdad   
        self.tipo = tipo    #tipo de propiedad
        self.precio = precio
        self.ambientes = ambientes
        self.propietario = propietario
        self.disponibilidad = "Disponible"
        self.identificador = identificador

    def __str__(self) -> str:
        return f" >> Id: {self.identificador} <<\n >> Barrio: {self.barrio} <<\n >> Tipo: {self.tipo} <<\n >> Ambientes: {self.ambientes} <<\n >> Precio: {self.precio} <<\n >> Propietario: {self.propietario} <<\n"
    
    def __eq__(self, other):
        return self.identificador == other.identificador
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.identificador<other.identificador
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.identificador<=other.identificador
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.identificador==other.identificador
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.identificador!=other.identificador
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.identificador>other.identificador
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.identificador>=other.identificador