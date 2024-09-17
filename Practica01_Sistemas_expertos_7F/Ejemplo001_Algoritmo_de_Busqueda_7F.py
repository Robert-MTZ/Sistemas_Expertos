# Ejemplo001_Algoritmo_de_Dijkstra
# Roberto_Martinez_Bailon_21310216_7F
# Ingenieria_en_Mecatronica

"""
Sobre el algoritmo implementado: dijkstra
El algoritmo de Dijkstra es un algoritmo clásico en informática y teoría de grafos que se utiliza para encontrar el camino más corto desde un nodo de origen a todos los demás nodos en un grafo ponderado (donde las aristas tienen pesos o costos). Fue propuesto por el científico holandés Edsger Dijkstra en 1956.

Características principales:
Funciona en grafos dirigidos o no dirigidos.
El grafo debe tener pesos no negativos en las aristas (si hay pesos negativos, Dijkstra no es adecuado, en ese caso se debe usar el algoritmo de Bellman-Ford).
Encuentra el camino más corto desde un nodo fuente a todos los demás nodos en el grafo.
Funcionamiento básico:
Se inicia desde un nodo fuente y se asigna un valor de costo de 0 a este nodo. A todos los demás nodos se les asigna un valor infinito.
El nodo fuente se marca como visitado, y se buscan sus vecinos directos, actualizando sus costos en función del costo del camino hasta ese punto.
Se selecciona el nodo no visitado con el menor costo y se repite el proceso para sus vecinos.
El algoritmo continúa hasta que todos los nodos han sido visitados y se hayan determinado los costos mínimos a cada uno.

"""

import heapq # La librería heapq en Python proporciona una implementación de colas de prioridad basadas en una estructura de datos llamada heap (montículo o montón). Un heap es una estructura de datos especializada que mantiene el orden parcial de sus elementos de manera que el elemento mínimo (en un min-heap) o máximo (en un max-heap) siempre esté en la raíz.

def dijkstra(graph, start):
    # Inicializamos las distancias con infinito para todos los nodos
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # La distancia al nodo inicial es 0
    # Usaremos un heap para seleccionar el nodo con la distancia mínima
    priority_queue = [(0, start)]  # (distancia, nodo)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si encontramos una distancia menor a la conocida, la actualizamos
        if current_distance > distances[current_node]:
            continue
        
        # Exploramos los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Si encontramos un camino más corto hacia el vecino, lo actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

if __name__ == "__main__":
    graph = {
        'Casa': {'Taller': 1, 'Almacen': 4},
        'Taller': {'Casa': 1, 'Almacen': 2, 'Refaccionaria': 5},
        'Almacen': {'Casa': 4, 'Taller': 2, 'Refaccionaria': 1},
        'Refaccionaria': {'Taller': 5, 'Almacen': 1}
    }
    
    start_node = 'Taller'
    shortest_distances = dijkstra(graph, start_node)
    
    print("**************************GPS**************************") # Se imprime mensaje inicial 
    print("Las distancia más corta desde: ", start_node) # Se imprime cual es la distancia mas corta
    for node, distance in shortest_distances.items():
        print(f"Distancia hacia: {node} es de {distance} km") # Se imprimen todas las distancias
