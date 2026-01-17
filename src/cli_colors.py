from enum import Enum


class Colors(Enum):
    """ANSI color codes for terminal text formatting.
    
    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
    El formato general es \033[Xm donde:
        \033 o \x1b es el carácter de escape
        X es el código del color/estilo
        Los códigos 30-37 son colores de texto normales
        Los códigos 90-97 son colores brillantes
        Los códigos 1-4 son para estilos de texto
    """
    # Foreground colors (texto)
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright foreground colors
    BRIGHT_BLACK = "\033[90m"  # Gray
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_PURPLE = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    # Styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # Reset
    RESET = "\033[0m"  # Más descriptivo que ENDC

    def __str__(self):
        return self.value
