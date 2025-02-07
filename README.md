# Algoritmos resolución de problemas mediante búsquedas.

## Ejercicios módulo Modelos de Intelixencia Artificial

### uso

`git clone https://github.com/dfleta/AI_101.git`

`python3 a_star`

### Ejercicio 1

Considérese el problema de encontrar un camino, en la situación representada en la figura, desde la posición $i$ hasta la posición $e$. El NPC (*non-player character*) puede moverse de forma horizontal y vertical, un solo cuadrado en cada movimiento (cada movimiento tiene coste uno). Las zonas sombreadas impiden el paso del NPC a través de ellas.

!["Mapa ejercicio 1"](./doc/mapa_ejercicio_1.png)


#### Consideraciones:

- Para aquellos algoritmos en los que no es relevante el coste, el orden de los operadores (movimientos) es: **arriba, abajo, izquierda, derecha**.
- Si algún algoritmo no controla los ciclos, supondremos que existen mecanismos para eliminarlos.
- El **coste del movimiento**:
  - **Vertical**: 1.
  - **Horizontal**: 2.
- Para el algoritmo **A** se utilizará la **distancia Manhattan** como heurística:

$$ h(n) = {distancia \ horizontal} + {distancia \ vertical} $$

- En el ejemplo, la distancia Manhattan entre $i$ y $e$ es $4$.

#### Representación de la solución:

- Resuelve el problema con cada uno de los algoritmos de búsqueda propuestos.
- Indica, para cada algoritmo, cuál se aplica para extraer los nodos de la frontera.
- Escribe:
  - La evolución del conjunto de nodos frontera.
  - El conjunto de nodos explorados durante el desarrollo del algoritmo.
  - La función coste y la heurística en los algoritmos que hagan uso de ellas.
- En la figura:
  - Nombra (enumera) los nodos según el orden en que son generados (incluidos en la frontera).
- Indica:
  - Cuándo la función test objetivo determina que el nodo chequeado es la solución.
  - La profundidad en la que se encuentra la solución.
- Razona y explica qué nodos y por qué conforman la solución.
- Representa:
  - El camino que conforma la solución (con una flecha en la figura).
  - El árbol de búsquedas.

### Ejercicio 2

#### Preguntas específicas:

1. La heurística utilizada en el algoritmo **A**, ¿es admisible? ¿Por qué?
   - ¿Podemos decir que el algoritmo es **A***?

### Consideraciones sobre la búsqueda A*

!["Evaluación de los algoritmos de búsquedas"](./doc/Evaluacion%20_algoritmos_busquedas.png)
Figura 3.15 Evaluación de los algoritmos de búsquedas. Russell y Norvig (2022)

!["Peso de la función heurística"](./doc/Heuristica_ponderada.png)
Epígrafe 3.5.4 "_Satisficing search: Inadmissible heuristics and weighted A*_". Russell y Norvig (2022)

!["A* ponderada"](./doc/A_ponderada.png)
Figura 3.15 Evaluación de los algoritmos de búsquedas. Russell y Norvig (2022)

## Bibliografía

Russell, S. J., & Norvig, P. (2022). _Artificial intelligence: a modern approach_. Global edition. Pearson Education Limited.
