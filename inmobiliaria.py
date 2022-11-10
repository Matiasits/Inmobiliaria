import pickle #libreria para guardar y recuperar informacion
from propiedad import Propiedad
from cliente import Cliente
from listas import *

#Inmobiliaria solo para propiedades de Cordoba Capital
class Inmobiliaria:
    #Atributos basicos de la inmobiliaria
    def __init__(self, operacion:str) -> None:
        self.operacion = operacion
        self.propiedades = Lista()
        self.clientes = Lista()    

    def alquilar_propiedad(self,propiedad,cliente) -> str:
        estado = ""
        if self.propiedades(propiedad) == "Disponible":
            #disponibilidad = "Alquilada"
            #estado = "Alquilada por {self.cliente}"
        else:
            #
            pass

#METODOS PARA PROPIEDADES
    def alta_propiedad(self,propiedad) -> None:
        self.propiedades.agregar(propiedad)
        pass
    
    def baja_propiedad(self,propietario) -> None:
        propiedad = self.propiedades.buscar(propietario)
        self.propiedades.remover(propiedad)
        pass
    
    def buscar_propiedad(self,propiedad) -> bool:
        return self.propiedades.buscar(propiedad)
        pass

    def cambiar_precio(self):
        pass

    def cambiar_estado(self):
        pass

#METODOS PARA CLIENTES
    def alta_cliente(self,cliente) -> None:
        self.clientes.agregar(cliente)
        pass

    def baja_cliente(self,cliente) -> None:
        c = self.clientes.buscar(cliente)
        self.clientes.remover(c)
        pass

    def buscar_cliente(self,cliente) -> bool:
        return self.clientes.buscar(cliente)


    """
    funcionalidades:
    dar alta cliente
    dar alta propiedad
    dar baja clientes
    dar baja propiedad 
    modificar cliente
    modificar propiedad
    modificar disponibilidad
    buscar clientes por dni
    buscar propiedad por barrio/tipo
    buscar propiedades dentro de cierto rango de precio
    buscar por operacion
    buscar propiedades por ambientes
    buscar por disponibilidad
    """