class Cliente:
    def __init__(self,dni:int,nombreCompleto:str,telefono:int,correo:str) -> None:
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.telefono = telefono
        self.correo = correo
    
    def __eq__(self,) -> bool:
        return self.dni == self.dni
    
    def __str__(self) -> str:
        return f"DNI: {self.dni}\nNombre Completo: {self.nombreCompleto}\nTelefono: {self.telefono}\nCorreo: {self.correo}"