# Ejemplo003_Algoritmo_Árbol_Parcial_mínimo_de_Prim
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""
El algoritmo de Kruskal es otro algoritmo codicioso utilizado para encontrar el árbol de expansión mínimo (MST, por sus siglas en inglés) en un grafo ponderado no dirigido. El MST es el subgrafo que conecta todos los nodos con el menor costo total posible sin formar ciclos.

A diferencia del algoritmo de Prim, que expande el MST desde un nodo inicial, Kruskal selecciona las aristas del grafo en orden creciente de peso, añadiéndolas al MST solo si no forman un ciclo.

Idea básica del algoritmo de Kruskal:
Se ordenan todas las aristas del grafo por peso en orden ascendente.
Se itera sobre las aristas, añadiendo cada arista al MST solo si no forma un ciclo.
Se utiliza una estructura de datos para rastrear las componentes conexas de los nodos, como el Union-Find (también llamado Disjoint Set Union o DSU) para gestionar eficientemente la unión y búsqueda de conjuntos de nodos.
El proceso continúa hasta que el MST tiene exactamente 𝑉−1 V−1 aristas (donde 𝑉 V es el número de nodos en el grafo).
Pasos del algoritmo de Kruskal:
Ordenar aristas: Ordena todas las aristas por sus pesos.
Inicializar conjuntos disjuntos: Cada nodo empieza en su propio conjunto (componente conectada).
Agregar aristas al MST:
Recorre las aristas en orden de peso. Si los nodos de una arista pertenecen a componentes diferentes, se agrega esa arista al MST y se combinan las dos componentes.
Si ambos nodos ya pertenecen a la misma componente, la arista se descarta para evitar ciclos.
Terminar: El proceso termina cuando se han agregado 𝑉−1 V−1 aristas al MST.
"""

import matplotlib.pyplot as plt # para crear gráficos y visualizaciones
import networkx as nx # se utiliza para importar la biblioteca networkx con el alias nx en Python. networkx es una librería ampliamente utilizada para la creación, manipulación y análisis de grafos y redes complejas

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal_mst_max_min(graph): # e utiliza una estructura de datos para rastrear las componentes conexas de los nodos, como el Union-Find (también llamado Disjoint Set Union o DSU) para gestionar eficientemente la unión y búsqueda de conjuntos de nodos
    edges = []
    for u in graph:
        for v, cost in graph[u].items():
            edges.append((cost, u, v))
    
    edges.sort()  # Ordenar aristas por costo (de menor a mayor)

    parent = {}
    rank = {}
    mst_min = []
    mst_max = []

    for node in graph:
        parent[node] = node
        rank[node] = 0

    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_min.append((u, v, cost))
            mst_max.append((u, v, cost))  # Para el máximo coste, simplemente se agregan todas las aristas
            print(f"Conexión establecida en MST Mínimo: {u} - {v}, Costo: {cost}")
            print(f"Secuencia de conexiones parcial en MST Mínimo: {mst_min}\n")

    return mst_min, mst_max

def draw_graph(graph, mst_edges_min, mst_edges_max):
    G = nx.Graph()

    for u in graph:
        G.add_node(u)

    for u, v, cost in mst_edges_min:
        G.add_edge(u, v, weight=cost)

    pos = nx.spring_layout(G)
    labels_min = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_min)

    plt.title('Árbol de Mínimo Coste para Organización de un Taller Mecánico')
    plt.show()

    G = nx.Graph()  # Nuevo grafo para el máximo coste

    for u in graph:
        G.add_node(u)

    for u, v, cost in mst_edges_max:
        G.add_edge(u, v, weight=cost)

    labels_max = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_max)

    plt.title('Árbol de Máximo Coste para Organización de un Taller Mecánico')
    plt.show()

# Ejemplo de grafo ponderado para organizar un taller mecánico
graph = {
    'AreaTB': {'Almacen': 6, 'Oficina': 5, 'Herramientas': 10},
    'Almacen': {'AreaTB': 6, 'Oficina': 4, 'Herramientas': 7},
    'Oficina': {'AreaTB': 5, 'Almacen': 4, 'Herramientas': 3},
    'Herramientas': {'AreaTB': 10, 'Almacen': 7, 'Oficina': 3}
}

# Calcular MST mínimo y máximo utilizando Kruskal para organizar un taller mecánico
mst_edges_min, mst_edges_max = kruskal_mst_max_min(graph)

# Mostrar gráficamente los MST mínimo y máximo
draw_graph(graph, mst_edges_min, mst_edges_max)
