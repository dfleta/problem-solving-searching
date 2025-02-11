class World:
    WORLD = [
        ["Y", "A", "B", "C", "D"],
        ["Z", "E", "F", "G", "H"],
        ["Ñ", "I", "-", "-", "L"],
        ["J", "-", "N", "O", "P"],
        ["K", "Q", "-", "S", "-"],
        ["M", "U", "V", "W", "X"],
    ]
    V_COST = 1
    H_COST = 2
    ROWS = len(WORLD)
    COLUMNS = len(WORLD[0])

    @classmethod
    def find_position(cls, state):
        for row in range(cls.ROWS):
            for col in range(cls.COLUMNS):
                if cls.WORLD[row][col] == state:
                    return row, col
        return None

    @classmethod
    def successors(cls, state):
        if state == "-":
            return []

        pos = cls.find_position(state)

        return cls.successor_function(*pos) if pos else []

    @classmethod
    def successor_function(cls, row, col):
        operators = [cls.up, cls.down, cls.left, cls.right]
        return list(filter(None, map(lambda operator: operator(row, col), operators)))

    @classmethod
    def up(cls, row, col):
        if row > 0 and cls.WORLD[row - 1][col] != "-":
            return (cls.WORLD[row - 1][col], cls.V_COST)

    @classmethod
    def down(cls, row, col):
        if row < cls.ROWS - 1 and cls.WORLD[row + 1][col] != "-":
            return (cls.WORLD[row + 1][col], cls.V_COST)

    @classmethod
    def left(cls, row, col):
        if col > 0 and cls.WORLD[row][col - 1] != "-":
            return (cls.WORLD[row][col - 1], cls.H_COST)

    @classmethod
    def right(cls, row, col):
        if col < cls.COLUMNS - 1 and cls.WORLD[row][col + 1] != "-":
            return (cls.WORLD[row][col + 1], cls.H_COST)
