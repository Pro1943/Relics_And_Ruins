import time
from rich.console import Console
from rich.align import Align
from rich.live import Live
from rich.text import Text

console = Console()

def titel():
    lines = [
        "  ▄▄▄▄▄▄         ▄▄                                        ▄▄▄▄▄▄                        ",
        " █▀██▀▀▀█▄        ██                                 █▄   █▀██▀▀▀█▄                      ",
        "   ██▄▄▄█▀        ██ ▀▀                     ▄        ██     ██▄▄▄█▀        ▀▀ ▄          ",
        "   ██▀▀█▄   ▄█▀█▄ ██ ██ ▄███▀ ▄██▀█   ▄▀▀█▄ ████▄ ▄████     ██▀▀█▄   ██ ██ ██ ████▄ ▄██▀█",
        " ▄ ██  ██   ██▄█▀ ██ ██ ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ▄ ██  ██   ██ ██ ██ ██ ██ ▀███▄",
        " ▀██▀  ▀██▀▄▀█▄▄▄▄██▄██▄▀███▄█▄▄██▀  ▄▀█▄██▄██ ▀█▄█▀███   ▀██▀  ▀██▀▄▀██▀█▄██▄██▄▀██▄▄██▀"
    ]

    color_palette = ["#00FFFF", "#00DFFF", "#00BFFF", "#009FFF", "#007FFF", "#005FFF", "#0000FF", "#005FFF", "#007FFF", "#009FFF", "#00BFFF", "#00DFFF"]

    frame = 0

    with Live(refresh_per_second=15, screen=False) as live:
        while True:
            text_block = Text()
            
            for i, line in enumerate(lines):
                color_index = (frame + i) % len(color_palette)
                current_color = color_palette[color_index]
                text_block.append(f"{line}\n", style=f"bold {current_color}")
            
            live.update(Align.center(text_block))
            time.sleep(0.058)
            frame += 1

titel()