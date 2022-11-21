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
        if self.propiedades.buscar(propiedad) and propiedad.disponibilidad == "Disponible":
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
        if self.buscar_propiedad(propiedad):
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

    def modificar_propiedad(self):
        pass

    #METODOS Clientes        
    def alta_cliente(self,dni) -> None:
        self.clientes.agregar(cliente)

    def baja_cliente(self,dni) -> None:
        if self.clientes.buscar(cliente) == True:
            self.clientes.remover(cliente)

    def buscar_cliente(self,dni) -> bool:
        return self.clientes.buscar(dni)
        
    def buscar_dato_cliente(self,cliente:object,dato:str): #devuelve objeto tipo dato
        print("Elija una opcion:\n1) General\n2) DNI\n3) Nombre\n4) Telefono\n5) Correo")

        opcion = int(input("Opcion: "))
        
        if opcion > 0 and opcion < 6:

            if self.buscar_cliente(cliente):
                datos = {
                    1 : cliente.__str__(),
                    2 : cliente.dni,
                    3 : cliente.nombreCompleto,
                    4 : cliente.telefono,
                    5 : cliente.correo,
                }
                if dato in datos:
                    print (f"{dato}: {datos[dato]}")
        else:
            print("No esta de alta")

    def modificar_cliente(self,cliente,opcion:int):
        


        datos = {   
                2 : cliente.dni,
                3 : cliente.nombreCompleto,
                4 : cliente.telefono,
                5 : cliente.correo,
            }
        pass

def guardar_archivo(inmobiliaria,archivo="inmobiliaria.pickle"):
    pickle_file = open(archivo, 'wb')
    pickle.dump(inmobiliaria, pickle_file)
    pickle_file.close()

def leer_archivo(inmobiliaria,archivo="inmobiliaria.pickle"):
    pickle_file = open(archivo,'rb')
    inmo = pickle.load(pickle_file)
    pickle_file.close()
    return inmo



#inmo.buscar_dato_cliente(c1,"nombre")

#inmo.buscar_dato_propiedad(p1,"tipo")
#inmo.buscar_dato_propiedad(p2,"tipo")
def menu():
    opcion = 0
    while opcion < 1 or opcion > 14:
        print("--")
        print("1 Dar de alta nuevo cliente")
        print("(2) Dar de baja cliente")
        print("(3) Buscar un cliente")
        print("(4) Modificar un cliente")
        print("(5) Dar de alta nueva propieda")
        print("(6) Dar de baja propiedad")
        print("(7) Buscar una propiedad")
        print("(8) Modificar una propiedad")
        print("(9) Alquilar propiedad")
        print("(10) Vender propiedad")
        print("(11) Guardar archivo")
        print("(12) Leer archivo")
        print("(13) Salir")
        # consultar pelicula - me devuelve la informacion de la pelicula
        print("--")
        opcion = int(input("Elija una opcion: "))
        print("--")
    return opcion


if __name__ == "__main__":
    inmobiliara = Inmobiliaria()

    opcion = 0

    while opcion != 12:
        opcion = menu()
    
        if opcion == 1:
            dni = int(input("Dni: "))
            nombreCompleto = input("Nombre Coompleto: ")
            telefono = int(input("Telefono: "))
            correo = input("Email: ")
            cliente = Cliente(dni,nombreCompleto,telefono,correo)
            if inmobiliara.buscar_cliente(cliente.dni):
                print("El cliente ya existe")
            else:
                inmobiliara.alta_cliente(cliente)
                print("Nuevo cliente")
    
        if opcion == 2:
            dni = input("Dni: ")
            if inmobiliara.buscar_cliente(dni):
                print(f"El cliente {dni} no existe")
            else:
                inmobiliara.baja_cliente(dni)
                print(f"Cliente {dni} ha sido dado de baja")
        
        if opcion == 3:
            dni = int(input("Dni: "))
            print(inmobiliara.buscar_cliente(dni))

        if opcion == 4:
            dni = int(input("Dni: "))
            print(inmobiliara.modificar_cliente(dni))

        if opcion == 5:
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = input("precio: ")
            ambientes = input("ambientes: ")
            propietario = input("propietario: ")
            propiedad = Propiedad(barrio,tipo,precio,ambientes,propietario)
            if inmobiliara.buscar_propiedad(propiedad.propietario):
                print("La propiedad ya esta dada de alta")
            else:
                inmobiliara.alta_propiedad(propiedad.propietario)
                print("Propiedad dada de alta")
        
        if opcion == 6:
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = input("precio: ")
            ambientes = input("ambientes: ")
            propietario = input("propietario: ")
            p = Propiedad(barrio,tipo,precio,ambientes,propietario)
            if inmobiliara.buscar_propiedad(p):
                print("La propiedad no esta dada de alta")
            
            else:
                inmobiliara.baja_propiedad(p)
                print("Propiedad ha sido dada de baja")
        
        if opcion == 7:
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = input("precio: ")
            ambientes = input("ambientes: ")
            propietario = input("propietario: ")
            p = Propiedad(barrio,tipo,precio,ambientes,propietario)

            print(inmobiliara.buscar_propiedad(p))
        
        if opcion == 8:
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = input("precio: ")
            ambientes = input("ambientes: ")
            propietario = input("propietario: ")
            p = Propiedad(barrio,tipo,precio,ambientes,propietario)
            
            if inmobiliara.buscar_propiedad(p):
                print("La pelicula no existe")
            else:
                print(inmobiliara.modificar_propiedad(p))

        if opcion == 9:
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = input("precio: ")
            ambientes = input("ambientes: ")
            propietario = input("propietario: ")
            p = Propiedad(barrio,tipo,precio,ambientes,propietario)
            

            if inmobiliara.buscar_propiedad(p) and inmobiliara.buscar_cliente(cliente.dni):
                inmobiliara.alquilar(p,cliente)
            
            else:
                print("No se encuentra disponible para alquilar")
        
        if opcion == 10:
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = input("precio: ")
            ambientes = input("ambientes: ")
            propietario = input("propietario: ")
            p = Propiedad(barrio,tipo,precio,ambientes,propietario)
            

            if inmobiliara.buscar_propiedad(p) and inmobiliara.buscar_cliente(cliente.dni):
                inmobiliara.vender(p,cliente)
            
            else:
                print("No se encuentra disponible para comprar")

        if opcion == 11:
            guardar_archivo(inmobiliara)
        if opcion == 12:
            inmo = leer_archivo(inmobiliara)

        if opcion == 13:
            break
