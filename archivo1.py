import csv
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
    def add_libro_static(libro:any,edit=0):
        if edit==0:
            Libro.list_libros.append(libro)
        else:
            indice=0
            for li in Libro.list_libros:
                if li.id==libro.id:
                   Libro.list_libros.remove(li)
                   break
                indice+=1   
            Libro.list_libros.insert(indice,libro)
    
    @staticmethod 
    def list_libros_static():
        for libro in Libro.list_libros:
            print(f"id:{libro.id},titulo:{libro.titulo},genero:{libro.genero},isbn:{libro.isbn},editorial:{libro.editorial},autores:{'-'.join(libro.autores)}")
    @staticmethod 
    def eliminar_libro_static(id=-1):
        if id==-1:
            Libro.list_libros.pop()
        else:
            for li in Libro.list_libros:
                if id==li.id:
                    Libro.list_libros.remove(li)
    @staticmethod               
    def busqueda_libro_static(busqueda):
        
            list_busqueda=[]
           
            for li in Libro.list_libros:
                 patron1 = re.search(f'{busqueda}+',str(li.isbn))
                 patron2 = re.search(f'{busqueda}+',str(li.titulo))
                 if patron1!=None or patron2!=None:
                     list_busqueda.append(li)
            print("quizas********")
            if list_busqueda!=[]:
                for libro in list_busqueda:
                    print(f"id:{libro.id},titulo:{libro.titulo},genero:{libro.genero},isbn:{libro.isbn},editorial:{libro.editorial},autores:{'-'.join(libro.autores)}")
            else:
                print("no existen concidencias")
    
    @staticmethod               
    def busqueda_libro_by_autor_editorial_genero_static(busqueda):
        
            list_busqueda=[]
           
            for libro in Libro.list_libros:
                 patron_autores     = re.search(f'{busqueda}+','-'.join(libro.autores))
                 patron_editorial   = re.search(f'{busqueda}+',str(libro.editorial))
                 patron_genero      = re.search(f'{busqueda}+',str(libro.genero))
                 if patron_autores!=None or patron_editorial!=None or patron_genero!=None:
                     list_busqueda.append(libro)
            print("quizas********")
            if list_busqueda!=[]:
                for libro in list_busqueda:
                    print(f"id:{libro.id},titulo:{libro.titulo},genero:{libro.genero},isbn:{libro.isbn},editorial:{libro.editorial},autores:{'-'.join(libro.autores)}")
            else:
                print("no existen concidencias")
                    
    @staticmethod
    def buscar_libro_by_cant_autores(cantidad):
            list_busqueda=[]
            for libro in Libro.list_libros:
                if len(libro.autores)==cantidad:
                    list_busqueda.append(libro)
            if list_busqueda!=[]:
                for libro in list_busqueda:
                    print(f"id:{libro.id},titulo:{libro.titulo},genero:{libro.genero},isbn:{libro.isbn},editorial:{libro.editorial},autores:{'-'.join(libro.autores)}")
            else:
                print("no existe tal cantidad autores en busqueda")
        
            
    @staticmethod 
    def ordenar_libro_static():
        Libro.list_libros=sorted(Libro.list_libros,key=lambda libro:libro.titulo)
        for libro in Libro.list_libros:
            print(f"id:{libro.id},titulo:{libro.titulo},genero:{libro.genero},isbn:{libro.isbn},editorial:{libro.editorial},autores:{'-'.join(libro.autores)}")

    @staticmethod
    def Escribir_libro_disco_static():
        
        with open('disco\escritura-disco.csv', 'w', newline='') as csvfile:

            fielheader = ['id', 'titulo','genero','isbn','editorial','autores']
            writer = csv.DictWriter(csvfile,fieldnames=fielheader)
            writer.writeheader()
            for libro in Libro.list_libros:
                writer.writerow({'id': libro.id, 'titulo':libro.titulo,'genero':libro.genero,'isbn':libro.isbn,'editorial':libro.editorial,'autores':'-'.join(libro.autores)})

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
    
    with open("Libros.csv", "r") as file:
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
    opciones=[li.id for li in Libro.list_libros]
    print(opciones)
    while(id_libro:=int(input("ingrese el id libro:")) not in opciones):
        print("no se encuentra el id")
        
    Libro.eliminar_libro_static(id_libro)
    print('Has elegido la opción 4')

def opcion5():
    busqueda=input("busqueda con ibsn/titulo libro:").strip()
    Libro.busqueda_libro_static(busqueda)
    print('Has elegido la opción 5')

def opcion6():
    Libro.ordenar_libro_static()
    print('Has elegido la opción 6')

def opcion7():
    busqueda=input("Busqueda con autor/editoria/genero libro:").strip()
    Libro.busqueda_libro_by_autor_editorial_genero_static(busqueda)
    print('Has elegido la opción 7')

def opcion8():
    cantidad=int(input("ingrese la cantidad de autores:").strip())
    Libro.buscar_libro_by_cant_autores(cantidad)
    print('Has elegido la opción 8')

def opcion9():
    fila={
        'id':int(input("ingrese identificador de edicion:")),
        'titulo':input("ingrese nuevo titulo:"),
        'genero':input("ingrese nuevo genero:"),
        'isbn' :int(input("ingrese nuevo isbn:")),
        'editorial':input("ingrese nuevo editorial:"),
        'autores':input("ingrese nuevo autores(separados por - example:auto1-autor2):").split('-')
    }
    
    libro=Libro(fila['id'],fila['titulo'],fila['genero'],fila['isbn'],fila['editorial'],fila['autores'])
    Libro.add_libro_static(libro,1)
    print('Has elegido la opción 9')

def opcion10():
    print('Has elegido la opción 10')

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()