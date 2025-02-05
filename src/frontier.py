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
