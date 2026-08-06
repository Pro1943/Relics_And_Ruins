from rich.console import Console
from rich.align import Align
from rich.live import Live
from rich.text import Text

console = Console()

def static_titel():
    lines = [
        r" _____      _ _                            _   _____       _             ",
        r"|  __ \    | (_)                          | | |  __ \     (_)            ",
        r"| |__) |___| |_  ___ ___    __ _ _ __   __| | | |__) |   _ _ _ __  ___   ",
        r"|  _  // _ \ | |/ __/ __|  / _` | '_ \ / _` | |  _  / | | | | '_ \/ __|  ",
        r"| | \ \  __/ | | (__\__ \ | (_| | | | | (_| | | | \ \ |_| | | | | \__ \  ",
        r"|_|  \_\___|_|_|\___|___/  \__,_|_| |_|\__,_| |_|  \_\__,_|_|_| |_|___/  "
    ]
    
    full_text = "\n".join(lines)
    plain_text = Text(full_text, style="bold #ad2df7")
    console.print(Align.center(plain_text))

static_titel()
