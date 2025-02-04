class Set:
    def __init__(self):
        self.elements = set()

    def add(self, node):
        self.elements.add(node)

    def remove(self, node):
        self.elements.discard(node)

    def contains(self, node):
        for element in self.elements:
            if element == node:
                return True
        return False

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def get_elements(self):
        return self.elements
