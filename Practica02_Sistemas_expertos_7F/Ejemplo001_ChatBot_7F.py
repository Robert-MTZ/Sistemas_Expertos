# Practica02_ChatBot
# CETI_COLOMOS_INGENIERIA
# ROBERTO_MARTINEZ_BAILON
# SISTEMAS_EXPERTOS_7F

import json # es un formato ligero y fácil de leer y escribir tanto para humanos como para máquinas

class Chatbot:
    def __init__(self):
        self.knowledge = {}

    def load_knowledge(self, filename):
        try:
            with open(filename, 'r') as file:
                self.knowledge = json.load(file)
        except FileNotFoundError:
            self.knowledge = {}

    def save_knowledge(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.knowledge, file)

    def chat(self, user_name):
        print(f"¡Hola, {user_name}! Estoy aprendiendo de ti.")
        
        while True:
            user_input = input(f"{user_name}: ")
            if user_input.lower() in ['salir', 'exit']:
                print("¡Hasta luego, espero volver a verte pronto y seguir aprendiendo de ti!!!")
                break
            elif user_input.lower() == 'ver informacion':
                self.show_knowledge(user_name)
            elif user_input.lower() == 'borrar informacion':
                self.delete_knowledge(user_name)
            else:
                self.learn(user_name, user_input)

    def learn(self, user_name, user_input):
        if ':' in user_input:
            key, value = user_input.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Inicializar el diccionario del usuario si no existe
            if user_name not in self.knowledge:
                self.knowledge[user_name] = {}

            # Guardar múltiples valores para la misma clave
            if key in self.knowledge[user_name]:
                if isinstance(self.knowledge[user_name][key], list):
                    self.knowledge[user_name][key].append(value)
                else:
                    self.knowledge[user_name][key] = [self.knowledge[user_name][key], value]
            else:
                self.knowledge[user_name][key] = value
            
            print(f"Aprendí que tu {key} es '{value}'.")
        else:
            print("No entendí eso. Usa el formato 'clave: valor' para enseñarme.")

    def show_knowledge(self, user_name):
        if user_name not in self.knowledge or not self.knowledge[user_name]:
            print("No he aprendido nada todavía.")
            return
        print("He aprendido lo siguiente:")
        for key, value in self.knowledge[user_name].items():
            print(f"{key}: {value}")

    def delete_knowledge(self, user_name):
        if user_name in self.knowledge:
            del self.knowledge[user_name]
            print(f"He borrado toda la información de {user_name}.")
        else:
            print("No hay información que borrar para este usuario.")

if __name__ == "__main__":
    bot = Chatbot()
    bot.load_knowledge('knowledge.json')

    while True:
        user_name = input("Introduce tu nombre (o 'salir' para terminar): ")
        if user_name.lower() in ['salir', 'exit']:
            break
        bot.chat(user_name)

    bot.save_knowledge('knowledge.json')
