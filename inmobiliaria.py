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

    def alquilar(self,p,c) -> str:
        if self.propiedades.buscar(p) and p.disponibilidad == "Disponible":
            p.disponibilidad = "Alquilada"
        return f"Alquilada a:\n{cliente.__str__()}"

    def vender(self,propiedad,c) -> str:
        if propiedad.disponibilidad == "Disponible":
            propiedad.disponibilidad = "Vendida"
            vendida_a = f"Vendida a:\n{cliente.__str__()}"
        return vendida_a


    #METODOS PARA PROPIEDADES
    def alta_propiedad(self,p) -> None:
        self.propiedades.agregar(p)

    def buscar_dato_propiedad(self,p): #devuelve objeto tipo dato
        if self.buscar_propiedad(p):
            pass
    def baja_propiedad(self,p) -> None:
        propiedad = self.propiedades.buscar(propietario)
        self.propiedades.remover(propiedad)

    def buscar_propiedad(self,p):
        return self.propiedades.buscar(p)

    def modificar_propiedad(self,p,nuevo_dato):
        return self.propiedades.asignar(p.dato,nuevo_dato)

    #METODOS Clientes        
    def alta_cliente(self,c) -> None:
        self.clientes.agregar(c)

    def baja_cliente(self,c) -> None:
        if self.clientes.buscar(c):
            self.clientes.remover(c)

    def buscar_cliente(self,c):
        return self.clientes.buscar(c)
        
    def buscar_dato_cliente(self,cliente:object,dato:str): #devuelve objeto tipo dato
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
        print(
            " 1 > Dar de alta nuevo cliente\n"
            " 2 > Dar de baja cliente\n"
            " 3 > Buscar un cliente\n"
            " 4 > Modificar un cliente\n"
            " 5 > Dar de alta nueva propiedad\n"
            " 6 > Dar de baja propiedad\n"
            " 7 > Buscar una propiedad\n"
            " 8 > Modificar una propiedad\n"
            " 9 > Alquilar propiedad\n"
            "10 > Vender propiedad\n"
            "11 > Guardar archivo\n"
            "12 > Leer archivo\n"
            "13 > Salir\n"
            )
        opcion = int(input("Elija una opcion: "))
        
    return opcion


if __name__ == "__main__":
    inmobiliaria = Inmobiliaria()



    opcion = 0

    while opcion != 12:
        opcion = menu()

        if opcion == 1:
            print("Ingrese los siguientes datos para dar de alta a un cliente")
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
            dni = int(input("Ingrese Dni para dar de baja a un cliente: "))
            if inmobiliaria.buscar_cliente(dni):
                print(f"El cliente {dni} no existe")
            else:
                inmobiliaria.baja_cliente(dni)
                print(f"Cliente {dni} ha sido dado de baja")
        
        if opcion == 3:
            dni = int(input("Ingrese Dni para buscar un cliente: "))
            c = Cliente(dni,'',0,'')
            print(inmobiliaria.buscar_cliente(c))

        if opcion == 4:
            dni = int(input("Ingrese Dni para modificar cliente: "))
            c = Cliente(dni,'',0,'')
            print(inmobiliaria.modificar_cliente(c))

        if opcion == 5:
            print("Ingrese los siguientes datos para dar de alta una propiedad")
            identificador = int(input("Id: "))
            barrio= input("barrio: ")
            tipo = input("tipo: ")
            precio = int(input("precio: "))
            ambientes = int(input("ambientes: "))
            propietario = int(input("propietario: "))
            p = Propiedad(barrio,tipo,precio,ambientes,propietario,identificador)
            
            if inmobiliaria.buscar_propiedad(p):
                print("La propiedad ya esta dada de alta")
            else:
                inmobiliaria.alta_propiedad(p)
                print("Propiedad dada de alta")

        if opcion == 6:
            identificador = int(input("Ingrese Id de la propiedad para darla de baja: "))
            p = Propiedad("","",0.0,"",0,identificador)
            
            
            if inmobiliaria.buscar_propiedad(p):
                print("La propiedad no esta dada de alta")
            else:
                inmobiliaria.baja_propiedad(p)
                print("Propiedad ha sido dada de baja")
        
        if opcion == 7:
            identificador = int(input("Ingrese Id de la propiedad para buscar la misma: "))
            p = Propiedad("","",0.0,"",0,identificador)
            print(inmobiliaria.buscar_propiedad(p))
        
        if opcion == 8:
            identificador = int(input("Ingrese Id de la propiedad a modificar: "))
            p = Propiedad("","",0.0,"",0,identificador)            
            
            seleccion = int(input(  "1 > Barrio\n"
                                    "2 > Tipo\n"
                                    "3 > Precio\n"
                                    "4 > Ambientes\n"
                                    "5 > Propietario\n"
                                    "6 > Disponibilidad\n"
                                    "Que desea modificar?: "
                                ))
            dato = ""

            if seleccion == 1:
                dato = "barrio"
            
            elif seleccion == 2:
                dato = "tipo"
            
            elif seleccion == 3:
                dato = "precio"
            
            elif seleccion == 4:
                dato = "ambientes"
                
            elif seleccion == 5:
                dato = "propietario"
                
            elif seleccion == 6:
                dato = "disponibilidad"

            nuevo_dato = input("Ingrese el nuevo dato a modificar: ")
            print(inmobiliaria.modificar_propiedad(p.dato,nuevo_dato))

        if opcion == 9:
            identificador = int(input("Id: "))
            p = Propiedad("","",0.0,"",0,identificador)            
            dni = int(input("Dni: "))
            c = Cliente(dni,'',0,'')

            if inmobiliaria.buscar_propiedad(p) and inmobiliaria.buscar_cliente(c):
                inmobiliaria.alquilar(p,c)
            else:
                print("No se encuentra disponible para alquilar")
        
        if opcion == 10:
            identificador = int(input("Id: "))
            p = Propiedad("","",0.0,"",0,identificador)
            
            dni = int(input("Dni: "))
            c = Cliente(dni,'',0,'')

            if inmobiliaria.buscar_propiedad(p) and inmobiliaria.buscar_cliente(c):
                inmobiliaria.vender(p,c)
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