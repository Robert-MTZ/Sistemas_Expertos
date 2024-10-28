import tkinter as tk
from tkinter import messagebox
import random

# Configuración de personajes, locaciones, y armas
personajes = {
    "Natalia": "cocinera",
    "Ricardo": "chofer",
    "Alberto": "jardinero",
    "Julián": "contratista",
    "Esteban": "abogado"
}

locaciones = ["Cocina", "Garaje", "Jardín", "Taller", "Despacho"]
armas = ["Cuchillo", "Llave española", "Pala", "Taladro", "Pistola"]

# Historias y pistas detalladas
historias = [
    {
        "escenario": "La Cena de Aniversario",
        "pistas_iniciales": {
            "personaje": "Alguien con acceso a la cocina fue visto entrando y saliendo frecuentemente.",
            "locacion": "El incidente ocurrió cerca de la cocina, y se escucharon ruidos desde el garaje.",
            "arma": "Parece que faltaba un cuchillo de cocina después del incidente."
        },
        "pistas_personajes": {
            "Natalia": "Natalia fue vista limpiando un cuchillo muy tarde en la noche.",
            "Ricardo": "Ricardo estaba moviendo cajas en el garaje justo antes del incidente.",
            "Alberto": "Alberto fue encontrado cubierto de tierra y algo nervioso en el jardín.",
            "Julián": "Julián dejó algunas herramientas mal colocadas en el taller.",
            "Esteban": "Esteban cerró la puerta del despacho y no dejó que nadie entrara durante la cena."
        },
        "pistas_locaciones": {
            "Cocina": "La cocina tenía restos de comida, y algunos utensilios faltaban.",
            "Garaje": "Se escucharon sonidos fuertes, como si alguien moviera cajas pesadas.",
            "Jardín": "Había huellas frescas en la tierra, como si alguien hubiera cavado recientemente.",
            "Taller": "Una herramienta parecía estar fuera de lugar.",
            "Despacho": "La puerta estaba cerrada con llave desde dentro."
        },
        "pistas_armas": {
            "Cuchillo": "Falta uno de los cuchillos grandes de la cocina.",
            "Llave española": "Esta herramienta suele estar en el garaje, pero hoy no estaba ahí.",
            "Pala": "La pala tenía tierra fresca cuando la encontraron.",
            "Taladro": "El taladro estaba fuera de lugar en el taller.",
            "Pistola": "La pistola de Esteban no estaba en su caja de seguridad."
        }
    },
    # Escenarios adicionales
    # (Agregue más escenarios con pistas detalladas de personajes, locaciones y armas)
]

# Variables para la historia y solución seleccionadas
historia_actual = None
asesino = locacion = arma = None

# Función para iniciar una nueva partida
def nueva_partida():
    global asesino, locacion, arma, historia_actual
    asesino = random.choice(list(personajes.keys()))
    locacion = random.choice(locaciones)
    arma = random.choice(armas)
    historia_actual = random.choice(historias)
    
    # Mostrar las pistas iniciales
    messagebox.showinfo(
        "Escenario",
        f"Escenario: {historia_actual['escenario']}\n\n"
        f"Pista de Personaje: {historia_actual['pistas_iniciales']['personaje']}\n"
        f"Pista de Locación: {historia_actual['pistas_iniciales']['locacion']}\n"
        f"Pista de Arma: {historia_actual['pistas_iniciales']['arma']}"
    )

    # Reiniciar las opciones seleccionadas
    sospechoso_var.set("Natalia")
    lugar_var.set("Cocina")
    arma_var.set("Cuchillo")

# Función para verificar la respuesta del usuario y mostrar pistas detalladas
def verificar_respuesta():
    sospechoso = sospechoso_var.get()
    lugar = lugar_var.get()
    arma_escogida = arma_var.get()
    
    if sospechoso == asesino and lugar == locacion and arma_escogida == arma:
        messagebox.showinfo("¡Felicidades!", f"¡Has resuelto el caso!\nEl asesino fue {asesino} ({personajes[asesino]}), "
                                             f"en el {locacion} con un(a) {arma}.")
        boton_reiniciar.pack(pady=5)
    else:
        pistas = []
        if sospechoso != asesino:
            pistas.append(f"Pista del personaje seleccionado: {historia_actual['pistas_personajes'][sospechoso]}")
        if lugar != locacion:
            pistas.append(f"Pista sobre la locación: {historia_actual['pistas_locaciones'][lugar]}")
        if arma_escogida != arma:
            pistas.append(f"Pista sobre el arma: {historia_actual['pistas_armas'][arma_escogida]}")
        messagebox.showwarning("Inténtalo de nuevo", "\n".join(pistas))

# Función para mostrar la ventana de personajes y ocupaciones
def mostrar_personajes():
    ventana_personajes = tk.Toplevel(ventana)
    ventana_personajes.title("Personajes y sus ocupaciones")
    ventana_personajes.geometry("300x250")
    
    tk.Label(ventana_personajes, text="Personajes y Ocupaciones", font=("Arial", 14)).pack(pady=10)
    
    for personaje, ocupacion in personajes.items():
        tk.Label(ventana_personajes, text=f"{personaje}: {ocupacion}", font=("Arial", 12)).pack(anchor="w", padx=10)
    
    tk.Button(ventana_personajes, text="Cerrar", command=ventana_personajes.destroy).pack(pady=10)

# Función para mostrar el mapa de locaciones
def mostrar_mapa():
    ventana_mapa = tk.Toplevel(ventana)
    ventana_mapa.title("Mapa de Locaciones")
    ventana_mapa.geometry("300x300")
    
    # Mapa sencillo usando etiquetas para representar cada locación
    tk.Label(ventana_mapa, text="Mapa de Locaciones", font=("Arial", 14)).pack(pady=10)
    
    mapa = """
       [Cocina]   [Despacho]
          |             |
       [Garaje]--[Taller]--[Jardín]
    """
    tk.Label(ventana_mapa, text=mapa, font=("Courier", 10)).pack(pady=10)
    
    tk.Button(ventana_mapa, text="Cerrar", command=ventana_mapa.destroy).pack(pady=10)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Clue")
ventana.geometry("500x550")

# Texto de introducción
tk.Label(ventana, text="Bienvenido al juego de Clue", font=("Arial", 16)).pack(pady=10)
tk.Label(ventana, text="Intenta adivinar quién es el asesino, dónde ocurrió y con qué arma", font=("Arial", 12)).pack()

# Botón para mostrar personajes y ocupaciones
boton_personajes = tk.Button(ventana, text="Ver personajes", command=mostrar_personajes, font=("Arial", 12), bg="purple", fg="white")
boton_personajes.pack(pady=10)

# Botón para mostrar el mapa de locaciones
boton_mapa = tk.Button(ventana, text="Ver Mapa de Locaciones", command=mostrar_mapa, font=("Arial", 12), bg="orange", fg="white")
boton_mapa.pack(pady=10)

# Selección de sospechoso
tk.Label(ventana, text="Selecciona al sospechoso:", font=("Arial", 12)).pack(pady=5)
sospechoso_var = tk.StringVar(value="Natalia")
sospechoso_menu = tk.OptionMenu(ventana, sospechoso_var, *personajes.keys())
sospechoso_menu.pack()

# Selección de locación
tk.Label(ventana, text="Selecciona la locación:", font=("Arial", 12)).pack(pady=5)
lugar_var = tk.StringVar(value="Cocina")
lugar_menu = tk.OptionMenu(ventana, lugar_var, *locaciones)
lugar_menu.pack()

# Selección de arma
tk.Label(ventana, text="Selecciona el arma:", font=("Arial", 12)).pack(pady=5)
arma_var = tk.StringVar(value="Cuchillo")
arma_menu = tk.OptionMenu(ventana, arma_var, *armas)
arma_menu.pack()

# Botón para verificar respuesta
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_respuesta, font=("Arial", 12), bg="green", fg="white")
boton_verificar.pack(pady=20)

# Botón para jugar otra vez
boton_reiniciar = tk.Button(ventana, text="Jugar otra vez", command=nueva_partida, font=("Arial", 12), bg="blue", fg="white")

# Botón para salir del juego
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, font=("Arial", 12), bg="red", fg="white")
boton_salir.pack(pady=5)

# Iniciar una nueva partida
nueva_partida()

# Iniciar el juego
ventana.mainloop()
