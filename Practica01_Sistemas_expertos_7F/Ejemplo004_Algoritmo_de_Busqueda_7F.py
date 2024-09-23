# Practica_001_Busqueda_Anchura_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica 

# Programa_Busqueda_Anchura_IA

from collections import deque # mandamos llamar el modulo "collections" para poder trabajar de una manera mas eficiente las estructuras de datos, tambien importamos "deque" para que admita inserciones y extracciones en ambos extremos

def ba(graf, inic, fin): # creamos una funcion llamada "ba" que seria la abreviatura de Busqueda en Anchura y le asignamos nuestras variables
    cola = deque() # Asignamos una variable para utilizar la estructura "deque()" la cual nos permite una insercion y eliminacion eficiente 
    visit = set() # De esta manera le asignamos una variable para que revise los elementos unicos y no ordenados  
    cola.append((inic, [inic])) # Este metodo se utiliza para agregar el elemento al final de un objeto

    while cola: # Creamos un ciclo que sera el que hara la busqueda 
        actual, path = cola.popleft() # esta linea se dedica a buscar nuestro parametro, "popleft()" es un metodo de la clase deque que extrae y devuelve el primer elemento de la cola, es decir, el elemento que se insertó primero en la cola
        visit.add(actual) # Esta linea nos ayudara a buscar entre nuestros datos 

        if actual == fin: # se cumple la condicion de mostrar nuestro elemento final
            return path # regresa al camino 

        for vecino in graf[actual]: # Este bucle itera sobre todos los vecinos del nodo actual actual en el grafo graf. graf[actual] devuelve una lista de todos los nodos adyacentes al nodo actual
            if vecino not in visit:  # Esta línea verifica si el vecino actual no ha sido visitado previamente. Si el vecino no está en el conjunto visit, significa que aún no ha sido procesado
                cola.append((vecino, path + [vecino])) # Si el vecino no ha sido visitado, se agrega a la cola junto con el nuevo camino que lleva a ese vecino. La cola almacena tuplas donde el primer elemento es el nodo vecino y el segundo elemento es el camino desde el nodo inicial hasta ese vecino. El nuevo camino se crea concatenando el camino existente (path) con el vecino actual. Esto asegura que el camino almacenado en la cola refleje el camino correcto desde el nodo inicial hasta el nodo actual

    return None # retornamos un valor nulo 

 # Asignamos valores a nuestra grafica para que tenga donde trabajar buestro ciclo (while)
if __name__== "__main__": # se usa para condicionar la ejecución de ciertas partes del código solo cuando el script se ejecuta de forma independiente
    graf = { 
        'I' : ['J', 'K'], # El nodo 'I' tiene conexiones con los nodos 'J' y 'K'.
        'J' : ['I', 'L', 'M'], #El nodo 'J' tiene conexiones con los nodos 'I', 'L' y 'M'. 
        'K' : ['I', 'N'], # El nodo 'K' tiene conexiones con los nodos 'I' y 'N'.
        'L' : ['J'], # El nodo 'L' tiene una conexión con el nodo 'J'.
        'M' : ['J', 'N'], # El nodo 'M' tiene conexiones con los nodos 'J' y 'N'.
        'N' : ['K', 'M'], # El nodo 'N' tiene conexiones con los nodos 'K' y 'M'.
    }

    inic_nodo = 'I' # Establecemos nuestro nodo inicial
    fin_nodo = 'N' # Establecemos nuestro nodo final 

    shortest_path = ba(graf, inic_nodo, fin_nodo) # Se buscara el camino mas corto entre los nodos 

    
   # Imprimimos nuestros resultados
    if shortest_path: # si se cumple entonces se imprimira el camino mas corto
        print(f"Lo distancia mas corta entre el nodo {inic_nodo} hasta el nodo {fin_nodo} es: {shortest_path}" )
    else: # Si no, se imprimira un mensaje de texto que avise al usuario que no existe un camino corto entre los nodos
        print(f"No existe el camino entre {inic_nodo} y {fin_nodo}")





    
