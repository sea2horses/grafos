# o Utiliza el grafo no dirigido del Ejercicio 1.
# o Realiza un bfs('A') y un dfs('A') y muestra los resultados.
# o Considera un grafo desconexo para probar cómo tus BFS/DFS se comportan (ej:
# agrega un vértice 'F' que no esté conectado a nada).

import auxiliar as aux

if __name__ == "__main__":
  grafo1 = aux.grafo1_nodirigido()
  
  # BFS
  print(grafo1.bfs('A'))
  # DFS
  print(grafo1.dfs('A'))
  
  # Agregare un nuevo vertice desconectado
  grafo1.agregar_vertice('F')
  
  # De nuevo
  # BFS
  print(grafo1.bfs('A'))
  # DFS
  print(grafo1.dfs('A'))