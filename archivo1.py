import re 
class Libro:
    list_libros:list[any] = []
    
    def __init__(self,id,titulo,genero,isbn,editorial,autores:list):
        self.id           = id
        self.titulo       = titulo
        self.genero       = genero
        self.isbn         = isbn
        self.editorial    = editorial
        self.autores      = autores
        
    @staticmethod 
    def add_libro_static(libro:any):
        Libro.list_libros.append(libro)
    
    @staticmethod 
    def list_libros_static():
        for libro in Libro.list_libros:
            print(f"id:{libro.id},titulo:{libro.titulo},genero:{libro.genero},autores:{libro.isbn},editorial:{libro.editorial},autores:{'-'.join(libro.autores)}")
    
    @staticmethod 
    def order_libros_titulo():
        libros = [libro.__dict__ for libro in Libro.list_libros]
        ordenados = sorted(libros, key=lambda l : l['titulo'])
        for l in ordenados:
            print(f"id => {l['id']}"
                  f"\nTitulo => {l['titulo']}")
            print("*" * 50)

    @staticmethod 
    def eliminar_libro_static(id=-1):
        if id==-1:
            Libro.list_libros.pop()
        else:
            for li in Libro.list_libros:
                if id==li.id:
                    print("entre a eliminar")
                    Libro.list_libros.remove(li)
    @staticmethod               
    def busqueda_libro_static(busqueda):
        
            list_busqueda=[]
            for li in Libro.list_libros:
                 patron1 = re.search(f"{busqueda}*",str(li.isbn))
                 patron2 = re.search(f"{busqueda}*",str(li.titulo))
                 if patron1!=None or patron2!=None:
                     list_busqueda.append(li)
            print("quizas********")
            if list_busqueda!=[]:
                for libro in list_busqueda:
                    print(f"id:{libro.id},titulo:{libro.titulo},genero:{libro.genero},autores:{libro.isbn},editorial:{libro.editorial},autores:{'-'.join(libro.autores)}")
        

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
    
    import csv

    with open("Libros.csv", "r") as file:
        Libro.list_libros.clear()
        reader = csv.DictReader(file)
        for fila in reader:
            list_autores=fila['autores'].split('-')
            libro=Libro(int(fila['id']),fila['titulo'],fila['genero'],fila['isbn'],fila['editorial'],list_autores)
            Libro.add_libro_static(libro)
    print('Has elegido la opción 1')

def opcion2():
    Libro.list_libros_static()
    print('Has elegido la opción 2')

def opcion3():
    fila={
        'id':int(input("ingrese identificador:")),
        'titulo':input("ingrese titulo:"),
        'genero':input("ingrese genero:"),
        'isbn' :int(input("ingrese isbn:")),
        'editorial':input("ingrese editorial:"),
        'autores':input("ingrese autores(separados por - example:auto1-autor2):").split('-')
    }
    
    libro=Libro(fila['id'],fila['titulo'],fila['genero'],fila['isbn'],fila['editorial'],fila['autores'])
    Libro.add_libro_static(libro)
    print('Has elegido la opción 3')

def opcion4():
    id_libro=int(input("ingrese el id libro:"))
    Libro.eliminar_libro_static(id_libro)
    print('Has elegido la opción 4')

def opcion5():
    busqueda=input("ingrese con ibsn/titulo libro:")
    Libro.busqueda_libro_static(busqueda)
    print('Has elegido la opción 5')

def opcion6():
    print('Has elegido la opción 6')
    Libro.order_libros_titulo()

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