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
            pass
    def baja_propiedad(self,propietario) -> None:
        propiedad = self.propiedades.buscar(propietario)
        self.propiedades.remover(propiedad)

    def buscar_propiedad(self,propiedad:object) -> bool:
        return self.propiedades.buscar(propiedad)

    def modificar_propiedad(self):
        pass

    #METODOS Clientes        
    def alta_cliente(self,c) -> None:
        self.clientes.agregar(c)

    def baja_cliente(self,c) -> None:
        if self.clientes.buscar(c):
            self.clientes.remover(c)

    def buscar_cliente(self,c):
        return self.clientes.buscar(c)
        
    def buscar_dato_cliente(self,cliente:object,dato:str): #devuelve objeto tipo dato
        #else:
         #   print("No esta de alta")
        pass
    def modificar_cliente(self,cliente,opcion:int):
        


        pass

def guardar_archivo(inmobiliaria,archivo="inmobiliaria.pickle"):
    pickle_file = open(archivo, 'wb')
    pickle.dump(inmobiliaria, pickle_file)
    pickle_file.close()

def leer_archivo(inmobiliaria,archivo="inmobiliaria.pickle"):
    pickle_file = open(archivo,'rb')
    inmobiliaria = pickle.load(pickle_file)
    pickle_file.close()
    return inmobiliaria



#inmo.buscar_dato_cliente(c1,"nombre")

#inmo.buscar_dato_propiedad(p1,"tipo")
#inmo.buscar_dato_propiedad(p2,"tipo")
def menu():
    opcion = 0
    while opcion < 1 or opcion > 14:
        print("1 > Dar de alta nuevo cliente\n2 > Dar de baja cliente\n3 > Buscar un cliente\n4 > Modificar un cliente\n5 > Dar de alta nueva propiedad\n6 > Dar de baja propiedad\n7 > Buscar una propiedad\n8 > Modificar una propiedad\n9 > Alquilar propiedad\n10 > Vender propiedad\n11 > Guardar archivo\n12 > Leer archivo\n13 > Salir")
        # consultar pelicula - me devuelve la informacion de la pelicula
        opcion = int(input("\nElija una opcion: "))
        
    return opcion


if __name__ == "__main__":
    inmobiliaria = Inmobiliaria()

    opcion = 0

    while opcion != 12:
        opcion = menu()

        if opcion == 1:
            dni = int(input("Dni: "))
            nombreCompleto = input("Nombre Coompleto: ")
            telefono = int(input("Telefono: "))
            correo = input("Email: ")
            
            cliente = Cliente(dni,nombreCompleto,telefono,correo)
            
            if inmobiliaria.buscar_cliente(cliente):
                print("El cliente ya existe")
            else:
                inmobiliaria.alta_cliente(cliente)
                print("Nuevo cliente")
    
        if opcion == 2:
            dni = int(input("Dni: "))
            if inmobiliaria.buscar_cliente(dni):
                print(f"El cliente {dni} no existe")
            else:
                inmobiliaria.baja_cliente(dni)
                print(f"Cliente {dni} ha sido dado de baja")
        
        if opcion == 3:
            dni = int(input("Dni: "))
            c = Cliente(dni,'',0,'')
            print(inmobiliaria.buscar_cliente(c))

        if opcion == 4:
            dni = int(input("Dni: "))
            print(inmobiliaria.modificar_cliente(dni))

        if opcion == 5:
            id = int(input("Id: "))
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = int(input("precio: "))
            ambientes = int(input("ambientes: "))
            propietario = int(input("propietario: "))
            propiedad = Propiedad(barrio,tipo,precio,ambientes,propietario,id)
            
            if inmobiliaria.buscar_propiedad(propiedad.propietario):
                print("La propiedad ya esta dada de alta")
            else:
                inmobiliaria.alta_propiedad(propiedad.propietario)
                print("Propiedad dada de alta")

        if opcion == 6:
            id = int(input("Id: "))
            propiedad = Propiedad("","",0.0,"",0,id)
            
            
            if inmobiliaria.buscar_propiedad(propiedad):
                print("La propiedad no esta dada de alta")
            else:
                inmobiliaria.baja_propiedad(propiedad)
                print("Propiedad ha sido dada de baja")
        
        if opcion == 7:
            id = int(input("Id: "))
            propiedad = Propiedad("","",0.0,"",0,id)
            
            print(inmobiliaria.buscar_propiedad(propiedad))
        
        if opcion == 8:
            id = int(input("Id: "))
            propiedad = Propiedad("","",0.0,"",0,id)            
            if inmobiliaria.buscar_propiedad(propiedad):
                print("La pelicula no existe")
            else:
                print(inmobiliaria.modificar_propiedad(propiedad))

        if opcion == 9:
            id = int(input("Id: "))
            propiedad = Propiedad("","",0.0,"",0,id)            
            dni = int(input("Dni: "))
            c = Cliente(dni,'',0,'')

            if inmobiliaria.buscar_propiedad(propiedad) and inmobiliaria.buscar_cliente(c):
                inmobiliaria.alquilar(propiedad,c)
            else:
                print("No se encuentra disponible para alquilar")
        
        if opcion == 10:
            id = int(input("Id: "))
            propiedad = Propiedad("","",0.0,"",0,id)
            
            dni = int(input("Dni: "))
            c = Cliente(dni,'',0,'')

            if inmobiliaria.buscar_propiedad(p) and inmobiliaria.buscar_cliente(c):
                inmobiliaria.vender(propiedad,c)
            else:
                print("No se encuentra disponible para comprar")

        if opcion == 11:
            guardar_archivo(inmobiliaria)

        if opcion == 12:
            inmo = leer_archivo(inmobiliaria)

        if opcion == 13:
            break

        print(f"\nClientes: {inmobiliaria.clientes.largo()}")
        print(f"Propiedades: {inmobiliaria.propiedades.largo()}\n")