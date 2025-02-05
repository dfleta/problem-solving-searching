class Map:
    def __init__(self):
        self.map = [
            ["Y", "A", "B", "C", "D"],
            ["Z", "E", "F", "G", "H"],
            ["Ñ", "I", "-", "-", "L"],
            ["LL", "-", "N", "O", "P"],
            ["AA", "Q", "-", "S", "-"],
            ["AB", "U", "V", "W", "X"],
        ]
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.v_cost = 1
        self.h_cost = 2

    def find_position(self, state):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.map[x][y] == state:
                    return x, y
        return None

    def successors(self, state):

        if state == "-":
            return []

        pos = self.find_position(state)
        if not pos:
            return []

        x, y = pos
        successors = []

        if x > 0 and self.map[x - 1][y] != "-":
            successors.append(
                (self.map[x - 1][y], self.v_cost)
            )  # Move up cost 1
        if x < self.rows - 1 and self.map[x + 1][y] != "-":
            successors.append(
                (self.map[x + 1][y], self.v_cost)
            )  # Move down
        if y > 0 and self.map[x][y - 1] != "-":
            successors.append(
                (self.map[x][y - 1], self.h_cost)
            )  # Move left cost 2
        if y < self.cols - 1 and self.map[x][y + 1] != "-":
            successors.append(
                (self.map[x][y + 1], self.h_cost)
            )  # Move right

        return successors
