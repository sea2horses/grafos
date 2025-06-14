from definiciones import Grafo

if __name__ == "__main__":
    # --- EJECUCIÓN DEL EJEMPLO COMPLETO ---

    # Creación de un grafo no dirigido y adición de aristas
    print("\n-- Creación de Grafo No Dirigido --")
    mi_grafo = Grafo(dirigido=False)

    mi_grafo.agregar_arista('Managua', 'Masaya')
    mi_grafo.agregar_arista('Managua', 'León')
    mi_grafo.agregar_arista('Masaya', 'Granada')
    mi_grafo.agregar_arista('Granada', 'Rivas')
    mi_grafo.agregar_arista('Managua', 'Granada') # Arista adicional para mayor conectividad

    # Imprimir la representación del grafo
    mi_grafo.imprimir_grafo()

    # Operaciones básicas: vecinos y existencia de aristas
    print("\n--- Operaciones Básicas ---")
    print(f"Vecinos de Managua: {mi_grafo.obtener_vecinos('Managua')}")
    print(f"¿Existe arista entre Managua y Masaya? {mi_grafo.obtener_aristas('Managua', 'Masaya')}")
    print(f"¿Existe arista entre Managua y Rivas? {mi_grafo.obtener_aristas('Managua', 'Rivas')}")

    # Recorridos BFS y DFS
    print("\n--- Recorridos ---")
    print(f"Orden de recorrido BFS desde Managua: {mi_grafo.bfs('Managua')}")
    print(f"Orden de recorrido DFS desde Managua: {mi_grafo.dfs('Managua')}")

    # Verificar conectividad y encontrar caminos
    print("\n--- Conectividad y Caminos ---")
    print(f"¿Es el grafo conexo? {mi_grafo.es_conexo()}")

    camino = mi_grafo.encontrar_camino('Managua', 'Rivas')
    print(f"Camino de Managua a Rivas: {camino}")

    camino_inexistente = mi_grafo.encontrar_camino('Managua', 'Juigalpa')
    print(f"Camino de Managua a Juigalpa: {camino_inexistente}")

    # Probar con un grafo dirigido
    print("\n--- Creación de Grafo Dirigido ---")
    grafo_dirigido = Grafo(dirigido=True)
    grafo_dirigido.agregar_arista('Inicio', 'A')
    grafo_dirigido.agregar_arista('A', 'B')
    grafo_dirigido.agregar_arista('B', 'C')
    grafo_dirigido.agregar_arista('C', 'Fin')
    grafo_dirigido.agregar_arista('Inicio', 'D')
    grafo_dirigido.agregar_arista('D', 'Fin')

    # Imprimir la representación del grafo dirigido
    grafo_dirigido.imprimir_grafo()

    # Consultar vecinos y existencia de aristas en el grafo dirigido
    print(f"\nVecinos de Inicio (Dirigido): {grafo_dirigido.obtener_vecinos('Inicio')}")
    print(f"Vecinos de Fin (Dirigido): {grafo_dirigido.obtener_vecinos('Fin')}") # Debería ser vacío
    print(f"¿Existe arista de A a B? {grafo_dirigido.obtener_aristas('A', 'B')}")
    print(f"¿Existe arista de B a A? {grafo_dirigido.obtener_aristas('B', 'A')}") # Debería ser False

    # Recorridos en el grafo dirigido
    print("\n--- Recorridos en Grafo Dirigido ---")
    print(f"Orden de recorrido BFS desde Inicio: {grafo_dirigido.bfs('Inicio')}")
    print(f"Orden de recorrido DFS desde Inicio: {grafo_dirigido.dfs('Inicio')}")

    # Verificar conectividad y caminos en el grafo dirigido
    print("\n--- Conectividad y Caminos en Grafo Dirigido ---")
    print(f"¿Es conexo el grafo dirigido? {grafo_dirigido.es_conexo()}") # Aplica a grafos dirigidos sin modificar la definición

    camino_dirigido = grafo_dirigido.encontrar_camino('Inicio', 'Fin')
    print(f"Camino dirigido de Inicio a Fin: {camino_dirigido}")

    camino_dirigido_no_existente = grafo_dirigido.encontrar_camino('Fin', 'Inicio')
    print(f"Camino dirigido de Fin a Inicio: {camino_dirigido_no_existente}")
