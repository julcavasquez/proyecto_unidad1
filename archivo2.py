# Peticion
import requests

class Pokemon:

    def __init__(self, name, habilidad, url_imagen):
        self.name = name
        self.habilidad:list[any] = habilidad
        self.url_imagen = url_imagen

    def mostrar_datos(self):
        print(f"Pokemon: {self.name}",
              f"\nHabilidades: {self.habilidad}",
              f"\nUrl_Imagen: {self.url_imagen}"
              )

def mostrar_menu(opciones):
    print('Menú de opciones:')
    for clave in opciones:
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Seleccionar Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Opción 1: Listar pokemons por generación.', opcion1),
        '2': ('Opción 2: Listar pokemons por forma.', opcion2),
        '3': ('Opción 3: Listar pokemons por habilidad.', opcion3),
        '4': ('Opción 4: Listar pokemons por habitat.', opcion4),
        '5': ('Opción 5: Listar pokemons por tipo.', opcion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')

# *** Definicion de funciones de cada opcion del menu ****
def opcion1():
    print('Has elegido la opción 1')

def opcion2():
    print('Has elegido la opción 2')

def opcion3():
    print('Has elegido la opción 3')

def opcion4():
    print('Has elegido la opción 4')

def opcion5():
    print('Has elegido la opción 5')

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()