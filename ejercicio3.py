# o Utiliza el grafo no dirigido del Ejercicio 1.
# o Verifica es_conexo().
# o Encuentra un camino de 'A' a 'E' y de 'A' a un vértice inexistente.

import auxiliar as aux

if __name__ == "__main__":
  # Crear grafo
  grafo1 = aux.grafo1_nodirigido()

  print(f"Es el grafo convexo? {grafo1.es_conexo()}")
  
  # Agregamos un vertice desconexo
  grafo1.agregar_vertice('F')

  print(f"Es el grafo convexo? {grafo1.es_conexo()}")

  # Camino de A a E
  print(f"Camino de 'A' a 'E': {grafo1.encontrar_camino('A','E')}")
  
  # Camino de A a X (nodo inexistente)
  print(f"Camino de 'A' a 'X': {grafo1.encontrar_camino('A','X')}")