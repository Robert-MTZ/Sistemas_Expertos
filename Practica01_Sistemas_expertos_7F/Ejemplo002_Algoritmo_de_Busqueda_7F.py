# Ejemplo002_Algoritmo_Árbol_Parcial mínimo_de_Prim
# Roberto_Martinez_Bailon_21310216_7F
# Ingenieria_en_Mecatronica

"""
El Algoritmo de Prim para obtener el Árbol de Expansión Mínimo (MST por sus siglas en inglés) es un algoritmo codicioso que busca conectar todos los nodos de un grafo ponderado de tal manera que se minimice la suma de los pesos de las aristas, sin formar ciclos.

¿Qué es un Árbol de Expansión Mínimo (MST)?
Es un subgrafo que incluye todos los nodos de un grafo original y algunas (o todas) las aristas, de forma que:

El subgrafo es un árbol (no tiene ciclos).
Conecta todos los nodos (es conexo).
La suma de los pesos de las aristas es la mínima posible entre todas las posibles combinaciones de aristas que forman un árbol.
Idea básica del algoritmo de Prim:
El algoritmo de Prim comienza desde un nodo cualquiera y crece el árbol de expansión mínimo añadiendo en cada paso una arista de menor peso que conecte un nodo que ya está en el árbol con uno que aún no lo está. El proceso se repite hasta que todos los nodos estén conectados.

Paso a paso del Algoritmo de Prim:
Inicialización:

Se selecciona un nodo inicial arbitrario.
Se inicializa un conjunto de nodos visitados y se agregan las aristas del nodo inicial a un heap (montón) de prioridad para seleccionar siempre la arista de menor peso.
Explorar aristas:

Se elige la arista de menor peso que conecte un nodo visitado con uno no visitado (usando el heap para gestionar esta selección de manera eficiente).
El nodo no visitado se marca como visitado y se agrega al árbol de expansión mínimo.
Se agregan las aristas que conectan al nuevo nodo con sus vecinos no visitados al heap de prioridad.
Repetir:

Se repite el proceso hasta que todos los nodos han sido visitados y el árbol de expansión mínimo cubre todos los nodos del grafo.
"""

import heapq
import matplotlib.pyplot as plt
import networkx as nx # networkx es una biblioteca de Python muy popular para la creación, manipulación y análisis de grafos y redes complejas

def prim_mst(graph): # Un árbol de expansión mínimo conecta todos los nodos de un grafo sin crear ciclos y minimizando la suma de los pesos de las aristas
    start_node = list(graph.keys())[0]
    visited = {start_node}
    edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node].items()]
    heapq.heapify(edges)
    mst = []

    while edges:
        cost, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))

            for neighbor, cost in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, v, neighbor))

        print(f"Visitando tarea: {u} - {v}, Prioridad: {cost}")
        print(f"Tareas incluidas en el MST parcial: {mst}")
        print(f"Tareas visitadas: {visited}\n")

    return mst

def draw_graph(graph, mst_edges):
    G = nx.Graph()

    for node in graph:
        G.add_node(node)

    for u, v, cost in mst_edges:
        G.add_edge(u, v, weight=cost)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.5, alpha=0.8, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.title('Árbol de Mínimo Coste para Organización de Tareas en un Taller Mecánico')
    plt.axis('off')
    plt.show()

graph = {
    'Reparación de Motor': {'Revisión de Frenos': 3, 'Cambio de Aceite': 4},
    'Revisión de Frenos': {'Reparación de Motor': 3, 'Cambio de Llantas': 2},
    'Cambio de Llantas': {'Revisión de Frenos': 2, 'Alineación de Dirección': 5},
    'Cambio de Aceite': {'Reparación de Motor': 4, 'Alineación de Dirección': 1},
    'Alineación de Dirección': {'Cambio de Llantas': 5, 'Cambio de Aceite': 1}
}

# Calcular MST utilizando el algoritmo de Prim
mst_edges = prim_mst(graph)

# Mostrar gráficamente el MST
draw_graph(graph, mst_edges)
