class Set:

    def __init__(self):
        self.elements = set()

    def add(self, node):
        self.elements.add(node)

    def remove(self, node):
        self.elements.discard(node)

    def contains(self, node):
        return any(element == node for element in self.elements)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.get_elements())

    def get_elements(self):
        return self.elements
