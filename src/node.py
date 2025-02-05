class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Coste desde el nodo inicial hasta este nodo
        self.h = (
            h  # Estimación del coste desde este nodo hasta el nodo objetivo
        )
        self.f = g + h  # Valor de la función objetivo f

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)

    def __repr__(self):
        return f"{self.state}"
