from src.collection import Set
from src.node import Node


class Frontier(Set):

    def __init__(self):
        super().__init__()

    def add(self, node):
        if isinstance(node, Node):
            super().add(node)

    def remove(self, node):
        if isinstance(node, Node):
            super().remove(node)

    def get_best_node(self):
        if self.is_empty():
            return None
        best_node = min(self.get_elements(), key=lambda node: node.f)
        self.remove(best_node)
        return best_node

    def get_node(self, node):
        return super().get_element(node)

    def update(self, node):
        if not isinstance(node, Node) or not self.contains(node):
            return None
        old = self.get_node(node)
        if node < old:
            self.__update_frontier(old, node)
            g_decrement = old.g - node.g
            self.__update_g(g_decrement, node)
        else:
            pass

    def __update_frontier(self, old, new):
        self.remove(old)
        self.add(new)

    def __update_g(self, g_decrement, new):
        for element in self.get_elements():
            if element.parent and element.parent.state == new.state:
                element.g -= g_decrement
                element.f = element.g + element.h
                self.__update_g(g_decrement, element)
