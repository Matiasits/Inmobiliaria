class Cliente:
    def __init__(self,dni:int,nombreCompleto:str,telefono:int,correo:str) -> None:
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.telefono = telefono
        self.correo = correo
    
    def __str__(self) -> str:
        return f" >> DNI: {self.dni}\n >> Nombre Completo: {self.nombreCompleto}\n >> Telefono: {self.telefono}\n >> Correo: {self.correo}\n"

    def __eq__(self,other):
        return self.dni == other.dni
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.dni<other.dni
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.dni<=other.dni
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.dni!=other.dni
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.dni>other.dni
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.dni>=other.dni