from collections import OrderedDict


class Set:
    def __init__(self):
        self.elements = OrderedDict()  # Mantiene el orden de inserción

    def add(self, node):
        self.elements[node] = None  # La clave es el nodo, el valor no importa

    def remove(self, node):
        self.elements.pop(node, None)

    def contains(self, node):
        return node in self.elements

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.elements)

    def get_elements(self):
        return list(self.elements.keys())  # Retorna las claves en orden de inserción

    def get_element(self, node):
        if node in self.elements:
            # como la igualdad del nodo se basa en el estado, devolvemos el nodo almacenado
            return list(filter(lambda k: k == node, self.get_elements()))[0]
        return None

    def clear(self):
        self.elements.clear()

    def __str__(self):
        return str([element.state for element in self.get_elements()])
