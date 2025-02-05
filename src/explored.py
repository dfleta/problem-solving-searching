from src.collection import Set
from src.node import Node

class Explored(Set):
    def __init__(self):
        super().__init__()

    def add(self, node):
        if isinstance(node, Node):
            super().add(node)

    def remove(self, node):
        if isinstance(node, Node):
            super().remove(node)

    def is_empty(self):
        return super().is_empty()

    def get_nodes(self):
        return self.get_elements()
