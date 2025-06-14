# PRUEBA DE IMPLEMENTACIÓN:
#
# o Crea una instancia de Grafo (no dirigido).
# o Agrega los vértices: 'A', 'B', 'C', 'D', 'E'.
# o Agrega las siguientes aristas: ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E').
# o Imprime los vecinos de 'A', 'D' y 'F' (para probar un vértice no existente).
# o Verifica si existe la arista ('A', 'C') y ('A', 'D').
# o Crea otra instancia de Grafo (dirigido).
# o Agrega aristas: ('X', 'Y'), ('Y', 'Z'), ('X', 'Z').
# o Imprime los vecinos de 'X' y 'Y'.

from definiciones import Grafo
import auxiliar as funcs

# Función principal
if __name__ == "__main__":
  # Crear el grafo
  grafo = funcs.grafo1_nodirigido()
  
  # Imprime los vecinos de los vertices
  print(f"Vecinos de A: {grafo.obtener_vecinos('A')}\nVecinos de D: {grafo.obtener_vecinos('D')}\nVecinos de F: {grafo.obtener_vecinos('F')}")
  
  # Verificacion de Aristas
  grafo.obtener_aristas('A', 'C')
  grafo.obtener_aristas('A', 'D')
  
  # Crear el otro grafo
  grafo_dirigido = funcs.grafo2_dirigido() 

  # Imprime los vecinos de X y Y
  print(f"Vecinos de X: {grafo_dirigido.obtener_vecinos('X')}\nVecinos de Y: {grafo_dirigido.obtener_vecinos('Y')}")