class World:

    WORLD = [
            ["Y", "A", "B", "C", "D"],
            ["Z", "E", "F", "G", "H"],
            ["Ñ", "I", "-", "-", "L"],
            ["LL", "-", "N", "O", "P"],
            ["AA", "Q", "-", "S", "-"],
            ["AB", "U", "V", "W", "X"],
        ]
    V_COST = 1
    H_COST = 2
    ROWS = len(WORLD)
    COLUMNS = len(WORLD[0])

    @classmethod
    def find_position(cls, state):
        for x in range(cls.ROWS):
            for y in range(cls.COLUMNS):
                if cls.WORLD[x][y] == state:
                    return x, y
        return None

    @classmethod
    def successors(cls, state):

        if state == "-":
            return []

        pos = cls.find_position(state)
        if not pos:
            return []

        x, y = pos
        successors = []

        if x > 0 and cls.WORLD[x - 1][y] != "-":
            successors.append(
                (cls.WORLD[x - 1][y], cls.V_COST)
            )  # Move up cost 1
        if x < cls.ROWS - 1 and cls.WORLD[x + 1][y] != "-":
            successors.append(
                (cls.WORLD[x + 1][y], cls.V_COST)
            )  # Move down
        if y > 0 and cls.WORLD[x][y - 1] != "-":
            successors.append(
                (cls.WORLD[x][y - 1], cls.H_COST)
            )  # Move left cost 2
        if y < cls.COLUMNS - 1 and cls.WORLD[x][y + 1] != "-":
            successors.append(
                (cls.WORLD[x][y + 1], cls.H_COST)
            )  # Move right

        return successors
