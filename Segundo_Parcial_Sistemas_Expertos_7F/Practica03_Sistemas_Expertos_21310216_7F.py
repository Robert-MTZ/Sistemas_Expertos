# Practica03_SistemasExpertos_21310216_7F
# Roberto Martinez Bailon
# Ingenieria en Mecatronica

import os # Manejo de archivos y directorios

# Archivo donde se guardarán los personajes
archivo_personajes = "personajes.txt"

# Diccionario con los personajes iniciales y sus atributos
personajes = {
    "Homero": ["torpe", "Hombre", "Amarillo", "Gordo", "Pelón", "Alcohólico"],
    "Bart": ["torpe", "Niño", "Amarillo"],
    "Marge": ["inteligente", "Mujer", "Amarillo", "Pelo azul"],
    "Lisa": ["inteligente", "Niña", "Amarillo", "Nerd"],
    "Moe": ["Hombre", "Amarillo", "Alcohólico", "Cantinero"],
    "Krusty": ["Hombre", "Gordo", "Alcohólico", "Payaso"],
    "Milhouse": ["inteligente", "Niño", "Amarillo", "Nerd", "Miope", "Pelo azul"]
}

# Lista de preguntas con sus respectivos atributos
preguntas = [
    ("¿Tu personaje es inteligente?", "inteligente"),
    ("¿Tu personaje es torpe?", "torpe"),
    ("¿Tu personaje es Hombre?", "Hombre"),
    ("¿Tu personaje es Mujer?", "Mujer"),
    ("¿Tu personaje es Niña?", "Niña"),
    ("¿Tu personaje es Niño?", "Niño"),
    ("¿Tu personaje es Amarillo?", "Amarillo"),
    ("¿Tu personaje es Gordo?", "Gordo"),
    ("¿Tu personaje es Pelón?", "Pelón"),
    ("¿Tu personaje es Nerd?", "Nerd"),
    ("¿Tu personaje es Alcohólico?", "Alcohólico"),
    ("¿Tu personaje tiene pelo azul?", "Pelo azul"),
    ("¿Tu personaje es un payaso?", "Payaso"),
    ("¿Tu personaje es miope?", "Miope"),
    ("¿Tu personaje es cantinero?", "Cantinero"),
    ("¿Tu personaje es una Bebé?", "Bebé"),
    ("¿Tu personaje es una Animal?", "Animal"), 
    ("¿Tu personaje es un perro?", "perro"),
    ("¿Tu personaje es un gato?", "gato"),
    ("¿Tu personaje es un monstruo?", "monstruo")
]

def cargar_personajes():
    """Carga personajes desde el archivo de texto si existe"""
    if os.path.exists(archivo_personajes):
        with open(archivo_personajes, "r") as file:
            for linea in file:
                nombre, atributos = linea.strip().split(":")
                personajes[nombre] = atributos.split(",")

def guardar_personajes():
    """Guarda los personajes en el archivo de texto"""
    with open(archivo_personajes, "w") as file:
        for nombre, atributos in personajes.items():
            file.write(f"{nombre}:{','.join(atributos)}\n")

def filtrar_personajes(personajes, atributo, respuesta):
    """Filtra personajes según el atributo y la respuesta del usuario"""
    return {nombre: attrs for nombre, attrs in personajes.items() if (atributo in attrs) == respuesta}

def agregar_personaje():
    """Permite al usuario agregar un nuevo personaje al juego"""
    nombre = input("Introduce el nombre del nuevo personaje: ").strip()
    if nombre in personajes:
        print("El personaje ya existe. Intenta con un nombre diferente.")
        return

    # Agregar atributos
    atributos = []
    for pregunta, atributo in preguntas:
        respuesta = input(f"{pregunta} (sí/no): ").strip().lower()
        if respuesta == "sí":
            atributos.append(atributo)
        elif respuesta != "no":
            print("Respuesta no válida. Se tomará como 'no'.")

    personajes[nombre] = atributos
    guardar_personajes()
    print(f"¡Personaje {nombre} agregado exitosamente con atributos: {', '.join(atributos)}!\n")

def borrar_personaje():
    """Permite al usuario borrar un personaje del juego y del archivo"""
    nombre = input("Introduce el nombre del personaje que deseas borrar: ").strip()
    if nombre in personajes:
        del personajes[nombre]
        guardar_personajes()
        print(f"¡Personaje {nombre} eliminado exitosamente!\n")
    else:
        print("El personaje no existe.")

def adivina_quien():
    print("Bienvenido al juego 'Adivina Quién' de Los Simpson!")
    cargar_personajes()
    jugar = True

    while jugar:
        print("\nLista de personajes:")
        print(", ".join(personajes.keys()))
        print("\nResponde las siguientes preguntas con 'sí' o 'no'.\n")
        
        # Copia de los personajes para ir descartando
        candidatos = personajes.copy()

        # Iterar sobre las preguntas
        for pregunta, atributo in preguntas:
            # Solo preguntar si hay más de un candidato
            if len(candidatos) > 1:
                respuesta = input(pregunta + " (sí/no): ").strip().lower()
                
                # Convertir respuesta a booleano
                if respuesta == "sí":
                    respuesta_bool = True
                elif respuesta == "no":
                    respuesta_bool = False
                else:
                    print("Respuesta no válida. Por favor responde 'sí' o 'no'.")
                    continue
                
                # Filtrar personajes en función de la respuesta
                candidatos = filtrar_personajes(candidatos, atributo, respuesta_bool)
                print(f"\nPersonajes restantes: {', '.join(candidatos.keys())}\n")
            else:
                break

        # Resultado final
        if len(candidatos) == 1:
            personaje = list(candidatos.keys())[0]
            print(f"¡Tu personaje es {personaje}!")
        elif len(candidatos) == 0:
            print("No hay personajes que coincidan con tus respuestas.")
        else:
            print("No se ha podido identificar al personaje con certeza.")
        
        # Opciones después de cada partida
        accion = input("¿Quieres jugar de nuevo, agregar un nuevo personaje, borrar un personaje o salir? (jugar/agregar/borrar/salir): ").strip().lower()
        if accion == "jugar":
            continue
        elif accion == "agregar":
            agregar_personaje()
        elif accion == "borrar":
            borrar_personaje()
        elif accion == "salir":
            jugar = False
            print("¡Gracias por jugar a 'Adivina Quién' con Los Simpson!")
        else:
            print("Opción no válida. El juego terminará.")
            jugar = False

adivina_quien() # Ejecutar el juego
