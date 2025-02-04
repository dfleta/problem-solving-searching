from src.collection import Set


class Explored(Set):
    def __init__(self):
        super().__init__()

    def add_node(self, node):
        self.add(node)

    def remove_node(self, node):
        self.remove(node)

    def contains_node(self, node):
        return self.contains(node)

    def is_empty(self):
        return super().is_empty()

    def size(self):
        return super().size()

    def get_nodes(self):
        return self.get_elements()
