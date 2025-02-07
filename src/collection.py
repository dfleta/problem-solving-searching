class Set:

    def __init__(self):
        self.elements = set()

    def add(self, node):
        self.elements.add(node)

    def remove(self, node):
        self.elements.discard(node)

    def contains(self, node):
        return node in self.get_elements()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.get_elements())

    def get_elements(self):
        return self.elements

    def get_element(self, node):
        return next(
            filter(lambda element: element == node, self.get_elements())
        )
    
    def __str__(self):
        return str([element.state for element in self.get_elements()])
