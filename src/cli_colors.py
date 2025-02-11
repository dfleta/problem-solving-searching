from enum import Enum


class Colors(Enum):
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    PURPLE = "\033[35m"
    ENDC = "\033[0m"

    def __str__(self):
        return self.value
