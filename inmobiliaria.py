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
        return f"\nAlquilada a:\n{self.buscar_cliente(c)}"

    def vender(self,p,c) -> str:
        if self.propiedades.buscar(p) and p.disponibilidad == "Disponible":
            p.disponibilidad = "Vendida"
        return f"\nVendida a:\n{self.buscar_cliente(c)}"
         
    #METODOS PARA PROPIEDADES
    def alta_propiedad(self,p) -> None:
        self.propiedades.agregar(p)

    def buscar_dato_propiedad(self, seleccion, p):
        p_auxiliar = self.buscar_propiedad(p)
        resultado = None
        if seleccion == 1:
            resultado = f"\nEl barrio es: {p_auxiliar.barrio}"

        elif seleccion == 2:
            resultado = f"\nEl tipo es: {p_auxiliar.tipo}"
                
        elif seleccion == 3:
            resultado = f"\nEl precio es: {p_auxiliar.precio}"
                
        elif seleccion == 4:
            resultado = f"\nLos ambientes son: {p_auxiliar.ambientes}"

        elif seleccion == 4:
            resultado = f"\nEl propietario es: {p_auxiliar.propietario}"

        elif seleccion == 4:
            resultado = f"\nDisponibilidad: {p_auxiliar.disponibilidad}"

        return resultado 

    def baja_propiedad(self,p) -> None:
        if self.propiedades.se_encuentra(p):
            self.propiedades.remover(p)

    def buscar_propiedad(self,p):
        return self.propiedades.buscar(p)

    def modificar_propiedad(self, seleccion, p, nuevo_dato):
        p_auxiliar = self.buscar_propiedad(p)
        
        if seleccion == 1:
            p_auxiliar.barrio = nuevo_dato
            
        elif seleccion == 2:
            p_auxiliar.tipo = nuevo_dato
            
        elif seleccion == 3:
            p_auxiliar.precio = nuevo_dato
            
        elif seleccion == 4:
            p_auxiliar.ambientes = nuevo_dato
                
        elif seleccion == 5:
            p_auxiliar.propietario = nuevo_dato
                
        elif seleccion == 6:
            p_auxiliar.disponibilidad = nuevo_dato

        return p_auxiliar.__str__()

    #METODOS Clientes        
    def alta_cliente(self,c) -> None:
        self.clientes.agregar(c)

    def baja_cliente(self,c) -> None:
        if self.clientes.se_encuentra(c):
            self.clientes.remover(c)

    def buscar_cliente(self,c):
        return self.clientes.buscar(c)
        
    def buscar_dato_cliente(self, seleccion, c):
        c_auxiliar = self.buscar_cliente(c)
        resultado = None
        if seleccion == 1:
            resultado = f"\nEl DNI es: {c_auxiliar.dni}"

        elif seleccion == 2:
            resultado = f"\nEl nombre completo es: {c_auxiliar.nombreCompleto}"
                
        elif seleccion == 3:
            resultado = f"\nEl telefono es: {c_auxiliar.telefono}"
                
        elif seleccion == 4:
            resultado = f"\nEl correo es: {c_auxiliar.correo}"

        return resultado

    def modificar_cliente(self, seleccion, c, nuevo_dato):
        c_auxiliar = self.buscar_cliente(c)
        
        if seleccion == 1:
            c_auxiliar.dni = nuevo_dato
            
        elif seleccion == 2:
            c_auxiliar.nombreCompleto = nuevo_dato
            
        elif seleccion == 3:
            c_auxiliar.telefono = nuevo_dato
            
        elif seleccion == 4:
            c_auxiliar.correo = nuevo_dato
                
        return c_auxiliar.__str__()

    def ordenar_cliente(self,orden): #ordena los clientes por edad
        lista = None
        if orden == 1:
            lista = self.clientes
        elif orden == 2:
            lista = self.propiedades

        for llenarRanura in range(lista.largo()-1,0,-1):
            posicionDelMayor = 0
            for ubicacion in range(1,llenarRanura+1):
                if lista.acceder(ubicacion) > lista.acceder(posicionDelMayor):
                    posicionDelMayor = ubicacion

            temp = lista.acceder(llenarRanura)
            lista.asignar(llenarRanura, lista.acceder(posicionDelMayor))
            lista.asignar(posicionDelMayor,temp)

        return lista.imprimir()
"""
def ordenamientoPorSeleccion(unaLista):
   for llenarRanura in range(len(unaLista)-1,0,-1):
       posicionDelMayor=0
       for ubicacion in range(1,llenarRanura+1):
           if unaLista[ubicacion]>unaLista[posicionDelMayor]:
               posicionDelMayor = ubicacion

       temp = unaLista[llenarRanura]
       unaLista[llenarRanura] = unaLista[posicionDelMayor]
       unaLista[posicionDelMayor] = temp
"""
def guardar_archivo(inmobiliaria,archivo="inmobiliaria.pickle"):
    pickle_file = open(archivo, 'wb')
    pickle.dump(inmobiliaria, pickle_file)
    pickle_file.close()

def leer_archivo(inmobiliaria,archivo="inmobiliaria.pickle"):
    pickle_file = open(archivo,'rb')
    inmobiliaria = pickle.load(pickle_file)
    pickle_file.close()
    return inmobiliaria



def menu():
    opcion = 0
    while opcion < 1 or opcion > 14:
        print(
            " 1 > Dar de alta nuevo cliente\n"
            " 2 > Dar de baja cliente\n"
            " 3 > Buscar un cliente\n"
            " 4 > Buscar dato de cliente\n"
            " 5 > Modificar un cliente\n"
            " 6 > Dar de alta nueva propiedad\n"
            " 7 > Dar de baja propiedad\n"
            " 8 > Buscar una propiedad\n"
            " 9 > Buscar dato de propiedad\n"
            "10 > Modificar una propiedad\n"
            "11 > Alquilar propiedad\n"
            "12 > Vender propiedad\n"
            "13 > Ordenar Clientes por edad\n"
            "14 > Guardar archivo\n"
            "15 > Leer archivo\n"
            "16 > Salir\n"
            )
        opcion = int(input("Elija una opcion: "))
        
    return opcion


if __name__ == "__main__":
    inmobiliaria = Inmobiliaria()

    opcion = 0

    while opcion != 16:
        opcion = menu()

        if opcion == 1:
            print("\nIngrese los siguientes datos para dar de alta a un cliente")
            dni = int(input(" > Dni: "))
            nombreCompleto = input(" > Nombre Completo: ")
            telefono = int(input(" > Telefono: "))
            correo = input(" > Email: ")
            
            cliente = Cliente(dni,nombreCompleto,telefono,correo)
            
            if inmobiliaria.buscar_cliente(cliente):
                print("El cliente ya existe")

            else:
                inmobiliaria.alta_cliente(cliente)
                print("\n>> Nuevo cliente de alta <<")
    
        if opcion == 2:
            dni = int(input("\nIngrese Dni para dar de baja a un cliente: "))
            c = Cliente(dni,'',0,'') #auxiliar
            
            inmobiliaria.baja_cliente(c)
            print(f"\n >> Cliente {dni} ha sido dado de baja << ")

        if opcion == 3:
            dni = int(input("\nIngrese Dni para buscar un cliente: "))
            c = Cliente(dni,'',0,'')
            print(f" >> Cliente encontrado! <<\n{inmobiliaria.buscar_cliente(c)}")
        
        if opcion == 4:
            dni = int(input("\nIngrese Dni para mostrar datos del cliente: "))
            c = Cliente(dni,'',0,'')

            seleccion = int(input(  "1 > DNI\n"
                                    "2 > Nombre Completo\n"
                                    "3 > Telefono\n"
                                    "4 > Correo\n"
                                    "Que desea mostrar?: "
                                ))
            print(f"\n >> Dato de cliente encontrado! <<\n{inmobiliaria.buscar_dato_cliente(seleccion,c)}")
        
        if opcion == 5:
            dni = int(input("\nIngrese Dni para modificar cliente: "))
            c = Cliente(dni,'',0,'')

            seleccion = int(input(  "1 > DNI\n"
                                    "2 > Nombre Completo\n"
                                    "3 > Telefono\n"
                                    "4 > Correo\n"
                                    "Que desea modificar?: "
                                ))

            nuevo_dato = input("\nIngrese el nuevo dato a modificar: ")
            print(f"\n >> Dato de cliente modificado con exito <<\n{inmobiliaria.modificar_cliente(seleccion ,c , nuevo_dato)}")

        if opcion == 6:
            print("\nIngrese los siguientes datos para dar de alta una propiedad")
            identificador = int(input(" >> Id: "))
            barrio= input(" >> Barrio: ")
            tipo = input(" >> Tipo: ")
            precio = int(input(" >> Precio: "))
            ambientes = int(input(" >> Ambientes: "))
            propietario = int(input(" >> Propietario: "))
            p = Propiedad(barrio,tipo,precio,ambientes,propietario,identificador)
            
            if inmobiliaria.buscar_propiedad(p):
                print("\nLa propiedad ya esta dada de alta")
            else:
                inmobiliaria.alta_propiedad(p)
                print("\n>> Nueva propiedad de alta <<")
       
        if opcion == 7:
            identificador = int(input("\nIngrese Id de la propiedad para darla de baja: "))
            p = Propiedad("","",0.0,"",0,identificador)
            
            inmobiliaria.baja_propiedad(p)
            print(f"\n >> Propiedad {identificador} ha sido dada de baja << ")        
        
        if opcion == 8:
            identificador = int(input("\nIngrese Id de la propiedad para buscar la misma: "))
            p = Propiedad("","",0.0,"",0,identificador)
            print(inmobiliaria.buscar_propiedad(p))
        
        if opcion == 9:
            identificador = int(input("\nIngrese Id de la propiedad para buscar la misma: "))
            p = Propiedad("","",0.0,"",0,identificador)

            seleccion = int(input(  "1 > Barrio\n"
                                    "2 > Tipo\n"
                                    "3 > Precio\n"
                                    "4 > Ambientes\n"
                                    "5 > Propietario\n"
                                    "6 > Disponibilidad\n"
                                    "Que desea mostrar?: "
                                ))

            print(f"\n >> Dato de propiedad encontrado! <<\n{inmobiliaria.buscar_dato_propiedad(seleccion, p)}")
        
        if opcion == 10:
            identificador = int(input("\nIngrese Id de la propiedad a modificar: "))
            p = Propiedad("","",0.0,"",0,identificador)            
            
            seleccion = int(input(  "1 > Barrio\n"
                                    "2 > Tipo\n"
                                    "3 > Precio\n"
                                    "4 > Ambientes\n"
                                    "5 > Propietario\n"
                                    "6 > Disponibilidad\n"
                                    "Que desea modificar?: "
                                ))

            nuevo_dato = input("\nIngrese el nuevo dato a modificar: ")
            print(f"\n >> Dato de propiedad modificado con exito <<\n{inmobiliaria.modificar_propiedad(seleccion ,p , nuevo_dato)}")

        if opcion == 11:
            identificador = int(input("\nIngrese el Id de la propiedad a alquilar: "))
            p = Propiedad("","",0.0,"",0,identificador)       

            dni = int(input("\nIngrese el Dni del cliente que alquilara: "))
            c = Cliente(dni,'',0,'')

            if inmobiliaria.buscar_propiedad(p) and inmobiliaria.buscar_cliente(c):
                print(inmobiliaria.alquilar(p,c))
            else:
                print("No se encuentra disponible para alquilar")
        
        if opcion == 12:
            identificador = int(input("\nIngrese el Id de la propiedad a comprar: "))
            p = Propiedad("","",0.0,"",0,identificador)
            dni = int(input("\nIngrese el Dni del cliente que comprara: "))
            c = Cliente(dni,'',0,'')

            if inmobiliaria.buscar_propiedad(p) and inmobiliaria.buscar_cliente(c):
                print(inmobiliaria.vender(p,c))
            else:
                print("No se encuentra disponible para comprar")

        if opcion == 13:
            orden = int(input(  "\nEsto ordenara de menor numero a mayor numero\n"
                                "1 > Clientes\n"
                                "2 > Propiedades\n"
                                "Que desea ordenar?: "
            ))
            inmobiliaria.ordenar_cliente(orden)

        if opcion == 14:
            guardar_archivo(inmobiliaria)

        if opcion == 15:
            leer_archivo(inmobiliaria)
            menu()

        if opcion == 16:
            break

        print(f"\nClientes: {inmobiliaria.clientes.largo()}")
        print(f"Propiedades: {inmobiliaria.propiedades.largo()}\n")
