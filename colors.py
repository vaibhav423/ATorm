class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    NUCLEUS = BRIGHT_RED
    PROTON = '\033[38;5;208m'
    NEUTRON = '\033[38;5;250m'
    ELECTRON = BRIGHT_CYAN
    
    SHELL_1 = BRIGHT_YELLOW
    SHELL_2 = BRIGHT_GREEN
    SHELL_3 = BRIGHT_BLUE
    SHELL_4 = BRIGHT_MAGENTA
    SHELL_5 = '\033[38;5;135m'
    SHELL_6 = '\033[38;5;201m'
    SHELL_7 = '\033[38;5;87m'
    
    HEADER = BRIGHT_CYAN
    INFO = CYAN
    HIGHLIGHT = BRIGHT_YELLOW
    ERROR = BRIGHT_RED
    SUCCESS = BRIGHT_GREEN

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')
