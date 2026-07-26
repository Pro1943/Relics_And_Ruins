import msvcrt
import time
from rich.console import Console
from rich.align import Align
from rich.live import Live
from rich.text import Text

console = Console()

def center_print(text: str, style: str):
    console.print(Align.center(text, style=style))

def wait_for_keypress_non_blocking():
    if msvcrt.kbhit():
        msvcrt.getch()
        return True
    return False

def clear_input_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

def titel():
    clear_input_buffer()
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
            if wait_for_keypress_non_blocking():
                break
            text_block = Text()
            for i, line in enumerate(lines):
                color_index = (frame + i) % len(color_palette)
                text_block.append(f"{line}\n", style=f"bold {color_palette[color_index]}")
            live.update(Align.center(text_block))
            time.sleep(0.06)
            frame += 1

def victory():
    clear_input_buffer()
    lines = [
        " █████ █████                        █████   ███   █████  ███             ███ ███",
        "░░███ ░░███                        ░░███   ░███  ░░███  ░░░             ░███░███",
        " ░░███ ███    ██████  █████ ████    ░███   ░███   ░███  ████  ████████  ░███░███",
        "  ░░█████    ███░░███░░███ ░███     ░███   ░███   ░███ ░░███ ░░███░░███ ░███░███",
        "   ░░███    ░███ ░███ ░███ ░███     ░░███  █████  ███   ░███  ░███ ░███ ░███░███",
        "    ░███    ░███ ░███ ░███ ░███      ░░░█████░█████░    ░███  ░███ ░███ ░░░ ░░░ ",
        "    █████   ░░██████  ░░████████       ░░███ ░░███      █████ ████ █████ ███ ███",
        "   ░░░░░     ░░░░░░    ░░░░░░░░         ░░░   ░░░      ░░░░░ ░░░░ ░░░░░ ░░░ ░░░ "
    ]
    color_palette = ["#004d00", "#007300", "#009900", "#00cc00", "#00ff00", "#33ff33", "#66ff66", "#99ff99", "#66ff66", "#33ff33", "#00ff00", "#00cc00", "#009900", "#007300"]
    frame = 0
    with Live(refresh_per_second=15, screen=False) as live:
        while True:
            if wait_for_keypress_non_blocking():
                break
            text_block = Text()
            for i, line in enumerate(lines):
                color_index = (frame + i) % len(color_palette)
                text_block.append(f"{line}\n", style=f"bold {color_palette[color_index]}")
            live.update(Align.center(text_block))
            time.sleep(0.035)
            frame += 1

def lost():
    clear_input_buffer()
    lines = [
        " █████ █████                        █████                         █████    ███ ███ ███",
        "░░███ ░░███                        ░░███                         ░░███    ░███░███░███",
        " ░░███ ███    ██████  █████ ████    ░███         ██████   █████  ███████  ░███░███░███",
        "  ░░█████    ███░░███░░███ ░███     ░███        ███░░███ ███░░  ░░░███░   ░███░███░███",
        "   ░░███    ░███ ░███ ░███ ░███     ░███       ░███ ░███░░█████   ░███    ░███░███░███",
        "    ░███    ░███ ░███ ░███ ░███     ░███      █░███ ░███ ░░░░███  ░███ ███░░░ ░░░ ░░░ ",
        "    █████   ░░██████  ░░████████    ███████████░░██████  ██████   ░░█████  ███ ███ ███",
        "   ░░░░░     ░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░  ░░░░░░     ░░░░░  ░░░ ░░░ ░░░ "
    ]
    color_palette = ["#4a0000", "#730000", "#9c0000", "#c50000", "#ef0000", "#ff2a2a", "#ff5555", "#ff8080", "#ff5555", "#ff2a2a", "#ef0000", "#c50000", "#9c0000", "#730000"]
    frame = 0
    with Live(refresh_per_second=15, screen=False) as live:
        while True:
            if wait_for_keypress_non_blocking():
                break
            text_block = Text()
            for i, line in enumerate(lines):
                color_index = (frame + i) % len(color_palette)
                text_block.append(f"{line}\n", style=f"bold {color_palette[color_index]}")
            live.update(Align.center(text_block))
            time.sleep(0.06)
            frame += 1
