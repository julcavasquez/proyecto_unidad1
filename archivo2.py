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
     api_pokemon_forma          = "https://pokeapi.co/api/v2/pokemon-shape/"
     reponse_forma_pokemon_list = requests.get(api_pokemon_forma)
     data_forma_pokemon_list    = reponse_forma_pokemon_list.json()
     opciones_forma_pokemon     = [forma['name'] for forma in data_forma_pokemon_list['results']]
     forma_pokemon=input(f"Ingrese la forma del pokemon >\nopciones:{opciones_forma_pokemon}:\n").strip()
     while (forma_pokemon not in opciones_forma_pokemon):
        print("¡La forma de pokemon no esta dentro de las opciones!")
        forma_pokemon = input(f"Ingrese la forma del pokemon > \nopciones:{opciones_forma_pokemon}:\n").strip()
    
     reponse_forma_pokemon_name  = requests.get(api_pokemon_forma +forma_pokemon+ "/")
     data_forma_pokemon = reponse_forma_pokemon_name.json()  
     print(f"****Lista de Pokemones de forma:{forma_pokemon}****")
     for pokemon_especies in data_forma_pokemon['pokemon_species']:
        response_pokemon_especie = requests.get(pokemon_especies['url'])
        data_pokemon_especie     = response_pokemon_especie.json()
        for pokemon in data_pokemon_especie['varieties']:
            varieties_pokemon    = requests.get(pokemon['pokemon']['url'])
            data_pokemon         = varieties_pokemon.json()
            MiPokemon = Pokemon(
                pokemon['pokemon']['name'],
                list(habilidad["ability"]["name"] for habilidad in data_pokemon["abilities"]),
                data_pokemon["sprites"]['front_default']
            )
            MiPokemon.mostrar_datos()
            print("-"*50)
    
     print('Has elegido la opción 2')

def opcion3():
    print('Has elegido la opción 3')
    api_pokemon_ability = "https://pokeapi.co/api/v2/ability/"
    contar = 2
    response_ability = requests.get(api_pokemon_ability)
    data_ability = response_ability.json()
    print(data_ability)
    print("****Lista de Habilidades de Pokemones****")
    for data in range(0, len(data_ability['results']) ,contar):
        print(f"[{data+1}]{data_ability['results'][data]['name']:<21} [{data+2}]{data_ability['results'][data+1]['name']:<19}")
    num_ability = lee_entero("Seleccione la habilidad del pokemon:")
    while (int(num_ability) == 0) or (int(num_ability) > 20):
        print("¡Ha seleccionado una habilidad-pokemon fuera del rango")
        num_ability = lee_entero("Seleccione una habilidad del pokemon:")
    print(api_pokemon_ability + str(int(num_ability)-1) + "/")
    response_ability_pokemon = requests.get(api_pokemon_ability + str(num_ability) + "/")
    data_ability_pokemon = response_ability_pokemon.json()  
    print(f"****Lista de Pokemones****")
    for pokemon in data_ability_pokemon['pokemon']:
        response_pokemon = requests.get(pokemon['pokemon']['url'])
        data_pokemon = response_pokemon.json()
        MiPokemon = Pokemon(
            data_pokemon["name"],
            list(habilidad["ability"]["name"] for habilidad in data_pokemon["abilities"]),
            data_pokemon["sprites"]['front_default']
        )
        MiPokemon.mostrar_datos()
        print("-"*50)

def opcion4():
     api_pokemon_habitat        = "https://pokeapi.co/api/v2/pokemon-habitat/"
     reponse_habitat_pokemon_list = requests.get(api_pokemon_habitat)
     data_habitat_pokemon_list    = reponse_habitat_pokemon_list.json()
     opciones_habitat_pokemon     = [habitat['name'] for habitat in data_habitat_pokemon_list['results']]
     habitat_pokemon=input(f"Ingrese el habitat del pokemon >\nopciones:{opciones_habitat_pokemon}:\n").strip()
     while (habitat_pokemon not in opciones_habitat_pokemon):
        print("¡El habitat de pokemon no esta dentro de las opciones!")
        habitat_pokemon = input(f"Ingrese el habitat del pokemon > \nopciones:{opciones_habitat_pokemon}:\n").strip()
    
     reponse_habitat_pokemon_name  = requests.get(api_pokemon_habitat +habitat_pokemon+ "/")
     data_habitat_pokemon = reponse_habitat_pokemon_name.json()
     print(f"****Lista de Pokemones de habitat:{habitat_pokemon}****")
     for pokemon_especies in data_habitat_pokemon['pokemon_species']:
        response_pokemon_especie = requests.get(pokemon_especies['url'])
        data_pokemon_especie     = response_pokemon_especie.json()
        for pokemon in data_pokemon_especie['varieties']:
            varieties_pokemon    = requests.get(pokemon['pokemon']['url'])
            data_pokemon         = varieties_pokemon.json()
            MiPokemon = Pokemon(
                pokemon['pokemon']['name'],
                list(habilidad["ability"]["name"] for habilidad in data_pokemon["abilities"]),
                data_pokemon["sprites"]['front_default']
            )
            MiPokemon.mostrar_datos()
            print("-"*50)
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