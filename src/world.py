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
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map[i][j] == state:
                    return i, j
        return None

    def successors(self, state):

        if state == "-":
            return []

        pos = self.find_position(state)
        if not pos:
            return []

        row, column = pos
        successors = []

        if row > 0 and self.map[row - 1][column] != "-":
            successors.append(
                (self.map[row - 1][column], self.v_cost)
            )  # Move up cost 1
        if row < self.rows - 1 and self.map[row + 1][column] != "-":
            successors.append(
                (self.map[row + 1][column], self.v_cost)
            )  # Move down
        if column > 0 and self.map[row][column - 1] != "-":
            successors.append(
                (self.map[row][column - 1], self.h_cost)
            )  # Move left cost 2
        if column < self.cols - 1 and self.map[row][column + 1] != "-":
            successors.append(
                (self.map[row][column + 1], self.h_cost)
            )  # Move right

        return successors
