from enum import Enum

class Colors(Enum):

    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[1;31;40m"
    YELLOW = "\033[1;33;40m"
    PURPLE =  "\033[1;35;40m"
    ENDC = "\033[0m"

    def __str__(self):
        return self.value
