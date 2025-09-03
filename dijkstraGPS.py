import heapq

def dijkstra(grafo, inicio, destino):
    # Distancias iniciales: infinito para todos menos el inicio
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0
    
    # Para reconstruir el camino
    previos = {nodo: None for nodo in grafo}
    
    # Cola de prioridad (distancia acumulada, nodo actual)
    cola = [(0, inicio)]
    
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si llegamos al destino, paramos
        if nodo_actual == destino:
            break

        # Si ya encontramos un camino más corto antes, saltamos
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Revisamos vecinos
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                previos[vecino] = nodo_actual
                heapq.heappush(cola, (distancia, vecino))
    
    # Reconstruir el camino
    camino = []
    nodo = destino
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = previos[nodo]
    
    return distancias[destino], camino

# Grafo de ejemplo (las calles)
grafo = {
    "Casa": {"Parque": 10, "Escuela": 15},
    "Parque": {"Casa": 10, "Escuela": 12, "Tienda": 5},
    "Escuela": {"Casa": 15, "Parque": 12, "Supermercado": 10},
    "Tienda": {"Parque": 5, "Supermercado": 7},
    "Supermercado": {"Escuela": 10, "Tienda": 7}
}

# Calculamos desde Casa al Supermercado
distancia, camino = dijkstra(grafo, "Casa", "Supermercado")

print(f"Distancia más corta: {distancia} metros")
print("Camino recomendado:", " → ".join(camino))
