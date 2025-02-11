# Algoritmos resolución de problemas mediante búsquedas.

## Ejercicios módulo Modelos de Intelixencia Artificial

### Uso

`https://github.com/dfleta/problem-solving-searching.git`

`python3 a_star -h`

```zsh
usage: a_star.py [-h] [-v_c V_C] [-h_c H_C] start_state goal_state

A* Search Algorithm

positional arguments:
  start_state  Initial state
  goal_state   Goal state

options:
  -h, --help   show this help message and exit
  -v_c V_C     Cost for vertical movements
  -h_c H_C     Cost for horizontal movements
```

#### Ejemplos

`python3 a_star.py -v_c 1 -h_c 2 Z N`

o 

`python3 a_star.py Z N`

!["CLI output Z N"](./doc/CLI_1.png)

`python3 a_star.py -v_c 1 -h_c 2 S F`

!["outpu CLI S F"](./doc/CLI_2.png)

### Algoritmo

!["Pseudocódigo A star I"](./doc/pseudocodigo_A_star_I.png)

!["Pseudocódigo A star II"](./doc/pseudocodigo_A_star_II.png)


El método `__update_g()` actualiza de manera recursiva todos los nodos de la frontera que son descendientes del nodo que se está actualizando. Veamos cómo funciona:

1. El método recibe dos parámetros:

   - `g_decrement`: la diferencia entre el valor g antiguo y el nuevo
   - `new`: el nodo que se acaba de actualizar

2. El proceso recursivo funciona así:

```py
   def __update_g(self, g_decrement, new):
       # Itera sobre todos los elementos en la frontera
       for element in self.get_elements():
           # Verifica si el elemento tiene un padre y si ese padre es el nodo que acabamos de actualizar
           if element.parent and element.parent.state == new.state:
               # Actualiza el valor g del elemento
               element.g -= g_decrement
               # Recalcula el valor f (f = g + h)
               element.f = element.g + element.h
               # Llamada recursiva para actualizar los hijos de este elemento
               self.__update_g(g_decrement, element)
```


La recursión ocurre porque:

1. Primero actualiza los hijos directos del nodo modificado

2. Para cada hijo actualizado, llama recursivamente a `__update_g()` para actualizar sus propios hijos

3. Este proceso continúa hasta que se hayan actualizado todos los descendientes en la frontera
Sí, el método `__update_g()` actualiza de manera recursiva todos los nodos de la frontera que son descendientes del nodo que se está actualizando. Veamos cómo funciona:

1. El método recibe dos parámetros:
   - `g_decrement`: la diferencia entre el valor g antiguo y el nuevo
   - `new`: el nodo que se acaba de actualizar

2. El proceso recursivo funciona así:
   ```py
   def __update_g(self, g_decrement, new):
       # Itera sobre todos los elementos en la frontera
       for element in self.get_elements():
           # Verifica si el elemento tiene un padre y si ese padre es el nodo que acabamos de actualizar
           if element.parent and element.parent.state == new.state:
               # Actualiza el valor g del elemento
               element.g -= g_decrement
               # Recalcula el valor f (f = g + h)
               element.f = element.g + element.h
               # Llamada recursiva para actualizar los hijos de este elemento
               self.__update_g(g_decrement, element)
   ```

La recursión ocurre porque:
1. Primero actualiza los hijos directos del nodo modificado
2. Para cada hijo actualizado, llama recursivamente a `__update_g()` para actualizar sus propios hijos
3. Este proceso continúa hasta que se hayan actualizado todos los descendientes en la frontera

Este proceso es necesario porque cuando se encuentra un camino más corto a un nodo, todos sus descendientes en el árbol de búsqueda también deben actualizarse para reflejar el nuevo costo del camino.


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
