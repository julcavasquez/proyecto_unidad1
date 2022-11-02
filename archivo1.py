class Libro:
    id = ''
    titulo = ''
    genero = ''
    isbn = ''
    editorial = ''
    autores = ''

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
        '1': ('Opción 1: Leer archivo de disco duro.', opcion1),
        '2': ('Opción 2: Listar Libros.', opcion2),
        '3': ('Opción 3: Agregar Libro.', opcion3),
        '4': ('Opción 4: Eliminar Libro.', opcion4),
        '5': ('Opción 5: Buscar libro por ISBN o por título.', opcion5),
        '6': ('Opción 6: Ordenar Libros por Titulo.', opcion6),
        '7': ('Opción 7: Buscar Libros por autor, editorial o género.', opcion7),
        '8': ('Opción 8: Buscar Libros por número de autores.', opcion8),
        '9': ('Opción 9: Editar o actualizar datos de un Libro.', opcion9),
        '10': ('Opción 10: Guardar libros en archivo de disco duro.', opcion10),
        '11': ('Salir', salir)
    }

    generar_menu(opciones, '11')

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

def opcion6():
    print('Has elegido la opción 6')

def opcion7():
    print('Has elegido la opción 7')

def opcion8():
    print('Has elegido la opción 8')

def opcion9():
    print('Has elegido la opción 9')

def opcion10():
    print('Has elegido la opción 10')

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()