# 🌐 Práctica de Grafos en Python

Bienvenido al repositorio de la **Práctica de Grafos**. Aquí encontrarás una implementación sencilla y didáctica de grafos en Python, con ejemplos de uso, documentación y explicaciones para facilitar el aprendizaje y la colaboración.

Integrantes:
- Farid Eduardo Zuñiga Rico
- Emilio Fernando Meza Ortiz
- Dennis Amaru Cruz Abrego
- Jose Nahum Espinoza Solano

---

## 🚀 Características

- **Grafo dirigido y no dirigido**
- **Agregar vértices y aristas**
- **Recorridos BFS y DFS**
- **Consulta de vecinos y aristas**
- **Verificación de conectividad**
- **Búsqueda de caminos entre nodos**
- **Código documentado y fácil de entender**
- **Ejemplos prácticos listos para ejecutar**

---

## 📂 Estructura del Proyecto

```
Grafos/
│
├── definiciones.py      # Implementación de la clase Grafo
├── ejemplo_grafo.py     # Ejemplo de uso y pruebas
├── README.md            # Este archivo
└── documento_proceso.md # Explicación del proceso realizado
```

---

## 🛠️ Requisitos

- Python 3.7 o superior

---

## ⚡ Uso Rápido

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/grafos-python.git
   cd grafos-python
   ```

2. **Ejecuta el ejemplo:**

   ```bash
   python ejemplo_grafo.py
   ```

3. **Explora y modifica los archivos para experimentar con tus propios grafos.**

---

## 📖 Ejemplo de Código

```python
from definiciones import Grafo

g = Grafo(dirigido=False)
g.agregar_arista('A', 'B')
g.agregar_arista('B', 'C')
g.imprimir_grafo()
print("BFS desde A:", g.bfs('A'))
print("DFS desde A:", g.dfs('A'))
```

---

## 👨‍💻 Colaboradores

- Integrante 1
- Integrante 2
- Integrante 3
- Integrante 4

¡Gracias a todos por su esfuerzo y dedicación!

---

## 📚 Recursos útiles

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Estructuras de datos en Python - GeeksforGeeks](https://www.geeksforgeeks.org/python-data-structures/)
- [Visualizador de grafos online](https://csacademy.com/app/graph_editor/)

---

## 📝 Licencia

Este proyecto es solo para fines educativos.

---

## ⭐ ¡Dale una estrella si te fue útil!

---
