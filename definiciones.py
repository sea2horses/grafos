from collections import deque

# Clase que representa un Grafo (dirigido o no dirigido)
class Grafo:
  # Constructor del grafo
  def __init__(self, dirigido = False):
    # Diccionario que almacena los nodos y sus conexiones (adyacencias)
    self.grafo = {}
    # Indica si el grafo es dirigido (True) o no dirigido (False)
    self.dirigido = dirigido
  
  # Método para agregar un vértice al grafo
  def agregar_vertice(self, vertice):
    # Si el vértice no existe, lo agrega
    if vertice not in self.grafo:
      # Se crea una entrada en el diccionario para el vértice con un conjunto vacío de vecinos
      self.grafo[vertice] = set()
      # Mensaje de confirmación
      print(f"Vertice ({vertice}) agregado.")
    else:
      # Mensaje si el vértice ya existe
      print(f"Vertice ({vertice}) ya existe.")
  
  # Método para agregar una arista entre dos vértices
  def agregar_arista(self, a, b, peso=1):
    # Asegura que ambos vértices existan en el grafo
    self.agregar_vertice(a)
    self.agregar_vertice(b)
    
    # Añade la arista a -> b
    self.grafo[a].add(b)
    print(f"Arista agregada ({a} -> {b})")
    
    # Si el grafo es no dirigido, añade también la arista b -> a
    if not self.dirigido:
      self.grafo[b].add(a)
      print(f"Arista agregada ({b} -> {a}) (bidireccional)")
  
  # Método para obtener los vecinos de un vértice
  def obtener_vecinos(self, vertice):
    # Devuelve la lista de vecinos si el vértice existe
    if vertice in self.grafo:
      return list(self.grafo[vertice])
    else:
      return []
  
  # Método para verificar si existe una arista entre dos vértices
  def obtener_aristas(self, a, b):
    # Retorna True si existe la arista de a hacia b
    return a in self.grafo and b in self.grafo[a]
  
  # Recorrido en anchura (BFS) desde un vértice inicial
  def bfs(self, inicio):
    visitados = set() # Conjunto de vértices visitados
    cola = deque() # Cola para el recorrido

    # Se inicia el recorrido desde el vértice inicial
    cola.append(inicio)
    visitados.add(inicio)
    
    recorrido = [] # Lista para almacenar el orden de visita
    
    while cola:
      vertice_actual = cola.popleft() # Extrae el primer elemento de la cola
      recorrido.append(vertice_actual)
      
      # Recorre todos los vecinos del vértice actual
      for vecino in self.obtener_vecinos(vertice_actual):
        if vecino not in visitados:
          visitados.add(vecino)
          cola.append(vecino)
    
    return recorrido
  
  # Recorrido en profundidad (DFS) desde un vértice inicial
  def dfs(self, inicio):
    visitados = set() # Conjunto de vértices visitados
    recorrido = [] # Lista para almacenar el orden de visita
    
    # Función recursiva interna para DFS
    def _dfs_recursivo(vertice):
      visitados.add(vertice)
      recorrido.append(vertice)

      for vecino in self.obtener_vecinos(vertice):
        if vecino not in visitados:
          _dfs_recursivo(vecino)
    
    # Inicia el DFS desde el vértice dado
    _dfs_recursivo(inicio)
    return recorrido
  
  # Método para imprimir la representación del grafo
  def imprimir_grafo(self):
    print("\n--- Representación del Grafo ---")
    for vertice, vecinos in self.grafo.items():
      # Muestra el vértice y sus vecinos
      print(f"{vertice}: {', '.join(vecinos)}")
    print("----------------------------")
  
  # Método para verificar si el grafo es conexo
  def es_conexo(self):
    # Un grafo vacío se considera conexo
    if not self.grafo:
      return True
    
    # Toma el primer vértice para iniciar el recorrido
    primer_vertice = next(iter(self.grafo))

    # Realiza un BFS desde el primer vértice
    recorrido_bfs = self.bfs(primer_vertice)

    # El grafo es conexo si se visitan todos los vértices
    return len(recorrido_bfs) == len(self.grafo)
  
  # Método para encontrar un camino entre dos vértices (usando BFS)
  def encontrar_camino(self, inicio, fin):
    # Verifica que ambos vértices existan en el grafo
    if inicio not in self.grafo or fin not in self.grafo:
      print(f"Error: '{inicio}' o '{fin}' no se encuentran en el grafo")
      return []
    
    cola = deque() # Cola para el recorrido
    visitados = set() # Conjunto de vértices visitados
    padres = {} # Diccionario para reconstruir el camino padres[hijo] = padre
    
    cola.append(inicio)
    visitados.add(inicio)
    padres[inicio] = None # El vértice inicial no tiene padre
    
    while cola:
      vertice_actual = cola.popleft()

      if vertice_actual == fin:
        # Si se llega al destino, se reconstruye el camino
        camino = []
        temp = fin
        while temp is not None:
          camino.append(temp)
          temp = padres[temp]
        
        return camino[::-1] # Devuelve el camino en orden correcto
      
      else:
        # Continúa explorando los vecinos
        for vecino in self.obtener_vecinos(vertice_actual):
          if vecino not in visitados:
            visitados.add(vecino)
            padres[vecino] = vertice_actual
            cola.append(vecino)
    
    # Si no se encuentra un camino, retorna lista vacía
    return []