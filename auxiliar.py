from definiciones import Grafo

def grafo1_nodirigido() -> Grafo: 
  # Crear el grafo
  grafo = Grafo()
  
  # Agregar vertices
  grafo.agregar_vertice('A')
  grafo.agregar_vertice('B')
  grafo.agregar_vertice('C')
  grafo.agregar_vertice('D')
  grafo.agregar_vertice('E')

  # Agregar aristas
  grafo.agregar_arista('A', 'B')
  grafo.agregar_arista('A', 'C')
  grafo.agregar_arista('B', 'D')
  grafo.agregar_arista('C', 'D')
  grafo.agregar_arista('D', 'E')

  return grafo

def grafo2_dirigido() -> Grafo: 
  # Crea otra instacia de grafo (dirigido)
  grafo_dirigido = Grafo(dirigido=True)

  # Agrega los vertices
  grafo_dirigido.agregar_vertice('X')
  grafo_dirigido.agregar_vertice('Y')
  grafo_dirigido.agregar_vertice('Z')
  
  # Agrega las aristas
  grafo_dirigido.agregar_arista('X', 'Y')
  grafo_dirigido.agregar_arista('Y', 'Z')
  grafo_dirigido.agregar_arista('X', 'Z')

  return grafo_dirigido