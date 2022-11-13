import pickle #libreria para guardar y recuperar informacion
from propiedad import Propiedad
from cliente import Cliente
from listas import *

#Inmobiliaria solo para propiedades de Cordoba Capital
class Inmobiliaria:
    #Atributos basicos de la inmobiliaria
    def __init__(self) -> None:
        self.propiedades = Lista()
        self.clientes = Lista()    

    def alquilar(self,propiedad:object,cliente:object) -> str:
        if propiedad.disponibilidad == "Disponible":
            propiedad.disponibilidad = "Alquilada"
        return f"Alquilada a:\n{cliente.__str__()}"

    def vender(self,propiedad,cliente) -> str:
        if propiedad.disponibilidad == "Disponible":
            propiedad.disponibilidad = "Vendida"
            vendida_a = f"Vendida a:\n{cliente.__str__()}"
        return vendida_a


    #METODOS PARA PROPIEDADES
    def alta_propiedad(self,propiedad) -> None:
        self.propiedades.agregar(propiedad)

    
    def buscar_dato_propiedad(self,propiedad:object,dato:str): #devuelve objeto tipo dato
        if self.buscar_propiedad(propiedad) == True:
            datos = {
                "barrio": propiedad.barrio,
                "tipo": propiedad.tipo,
                "precio": propiedad.precio,
                "ambientes": propiedad.ambientes,
                "propietario": propiedad.propietario,
                "disponibilidad": propiedad.disponibilidad
            }
            if dato in datos:
                print (f"{dato}: {datos[dato]}")
        else:
            print("No esta de alta")

    def baja_propiedad(self,propietario) -> None:
        propiedad = self.propiedades.buscar(propietario)
        self.propiedades.remover(propiedad)

    def buscar_propiedad(self,propiedad:object) -> bool:
        return self.propiedades.buscar(propiedad)
        

    def cambiar_precio(self,nuevo_precio:int,propiedad:object) -> None:
        if self.propiedades.buscar(propiedad) == True:
            propiedad.precio = nuevo_precio
        return propiedad.precio

    #METODOS Clientes        
    def alta_cliente(self,cliente) -> None:
        self.clientes.agregar(cliente)


    def baja_cliente(self,cliente) -> None:
        if self.clientes.buscar(cliente) == True:
            self.clientes.remover(cliente)

    def buscar_cliente(self,cliente) -> bool:
        return self.clientes.buscar(cliente)
        
    def buscar_dato_cliente(self,cliente:object,dato:str): #devuelve objeto tipo dato
        if self.cliente(cliente) == True:
            datos = {
                "dni": cliente.dni,
                "nombre": cliente.nombreCompleto,
                "telefono": cliente.telefono,
                "correo": cliente.correo,
            }
            if dato in datos:
                print (f"{dato}: {datos[dato]}")
        else:
            print("No esta de alta")

inmo = Inmobiliaria()
p1 = Propiedad("nva cordoba","depto",12000,1,41712653)
p2 = Propiedad("villa libertador","casa",24000,1,41712653)


c1 = Cliente(41712653,"nasmidasd",123123,"asdfgaf@FASDFASF")
c2 = Cliente(25712653,"asd",123,"@aFASDFASF")

inmo.alta_propiedad(p1)
inmo.alta_propiedad(p2)

inmo.alta_cliente(c1)
inmo.alta_cliente(c2)

print(inmo.buscar_cliente(c1))
print(inmo.buscar_cliente(c2))

inmo.buscar_dato_propiedad(p1,"tipo")
inmo.buscar_dato_propiedad(p2,"tipo")