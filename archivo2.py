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

def lee_entero(msg):
    while True:
        valor = input(f"{msg}")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print ("Debe ingresar un número")
            
# *** Definicion de funciones de cada opcion del menu ****
api_pokemon = "https://pokeapi.co/api/v2/pokemon/"
def opcion1():
    generacion = lee_entero("Ingrese una generación (1-8):")
    while (int(generacion) == 0) or (int(generacion) > 8):
        print("¡Ha escrito una generación fuera del rango")
        generacion = lee_entero("Ingrese una generación (1-8):")
    api_generacion = "https://pokeapi.co/api/v2/generation/" + str(generacion) + "/"
    response = requests.get(api_generacion)
    data = response.json()
    print(f"****Lista de Pokemones****")
    for pokemon in data['pokemon_species']:
        response_pokemon = requests.get(api_pokemon + pokemon['name'])
        data_pokemon = response_pokemon.json()
        MiPokemon = Pokemon(
            data_pokemon["name"],
            list(habilidad["ability"]["name"] for habilidad in data_pokemon["abilities"]),
            data_pokemon["sprites"]['front_default']
        )
        MiPokemon.mostrar_datos()
        print("-"*50)

def opcion2():
    print('Has elegido la opción 2')

def opcion3():
    print('Has elegido la opción 3')

def opcion4():
    print('Has elegido la opción 4')

def opcion5():
    print('Has elegido la opción 5')
    api_pokemon_tipo = "https://pokeapi.co/api/v2/type/"
    contar = 2
    response_tipo = requests.get(api_pokemon_tipo)
    data_tipo = response_tipo.json()
    print("****Lista de Tipos de Pokemons****")
    for data in range(0, len(data_tipo['results']) ,contar):
        print(f"[{data+1}]{data_tipo['results'][data]['name']:<21} [{data+2}]{data_tipo['results'][data+1]['name']:<19}")
    num_tipo = lee_entero("Seleccione un tipo de pokemon:")
    while (int(num_tipo) == 0) or (int(num_tipo) > 20):
        print("¡Ha seleccionado un tipo-pokemon de fuera del rango")
        num_tipo = lee_entero("Seleccione un tipo de pokemon:")
    print(api_pokemon_tipo + str(int(num_tipo)-1) + "/")
    response_tipo_pokemon = requests.get(api_pokemon_tipo + str(num_tipo) + "/")
    data_tipo_pokemon = response_tipo_pokemon.json()  
    print(f"****Lista de Pokemones****")
    for pokemon in data_tipo_pokemon['pokemon']:
        response_pokemon = requests.get(pokemon['pokemon']['url'])
        data_pokemon = response_pokemon.json()
        MiPokemon = Pokemon(
            data_pokemon["name"],
            list(habilidad["ability"]["name"] for habilidad in data_pokemon["abilities"]),
            data_pokemon["sprites"]['front_default']
        )
        MiPokemon.mostrar_datos()
        print("-"*50)


def salir():
    print('Has elegido la opcion salir')


if __name__ == '__main__':
    menu_principal()