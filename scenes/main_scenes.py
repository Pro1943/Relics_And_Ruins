import msvcrt
import time
from rich.console import Console, Group
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

def center_lines(lines, colors, frame):
    text_block = Text()

    for i, line in enumerate(lines):
        color = colors[(frame + i) % len(colors)]
        text_block.append(
            f"{line}\n",
            style=f"bold {colors[(frame + i) % len(colors)]}"
        )

    return Align.center(text_block)

def animated_title(lines, colors, speed):
    clear_input_buffer()

    frame = 0

    with Live(refresh_per_second=30, screen=False, auto_refresh=False) as live:
        while True:
            if wait_for_keypress_non_blocking():
                break

            width = console.width
            height = console.height

            logo_width = max(len(line) for line in lines)
            logo_height = len(lines)

            left_padding = max((width - logo_width) // 2, 0)
            top_padding = max((height - logo_height - 2) // 2, 0)

            text = Text()

            text.append("\n" * top_padding)

            for i, line in enumerate(lines):
                color = colors[(frame + i) % len(colors)]
                text.append(" " * left_padding)
                text.append(line, style=f"bold {color}")
                text.append("\n")

            text.append("\n")
            text.append(" " * max((width - len("Press any key to continue...")) // 2, 0))
            text.append(
                "Press any key to continue...",
                style="bold cyan"
            )

            live.update(text, refresh=True)

            time.sleep(speed)
            frame += 1

def title():
    lines = [
        "    ▄▄▄▄▄▄          ▄▄                                        ▄▄▄▄▄▄                       ",
        "   █▀██▀▀▀█▄        ██                                 █▄   █▀██▀▀▀█▄                      ",
        "     ██▄▄▄█▀        ██ ▀▀                      ▄       ██     ██▄▄▄█▀        ▀▀ ▄          ",
        "     ██▀▀█▄   ▄█▀█▄ ██ ██ ▄███▀ ▄██▀█   ▄▀▀█▄ ████▄ ▄████     ██▀▀█▄   ██ ██ ██ ████▄ ▄██▀█",
        "   ▄ ██  ██   ██▄█▀ ██ ██ ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ▄ ██  ██   ██ ██ ██ ██ ██ ▀███▄",
        "   ▀██▀  ▀██▀▄▀█▄▄▄▄██▄██▄▀███▄█▄▄██▀  ▄▀█▄██▄██ ▀█▄█▀███   ▀██▀  ▀██▀▄▀██▀█▄██▄██▄▀██▄▄██▀"
    ]

    colors = [
        "#00FFFF",
        "#00DFFF",
        "#00BFFF",
        "#009FFF",
        "#007FFF",
        "#005FFF",
        "#0000FF",
        "#005FFF",
        "#007FFF",
        "#009FFF",
        "#00BFFF",
        "#00DFFF"
    ]

    animated_title(lines, colors, 0.06)


def victory():
    lines = [
        " █████ █████                        █████   ███   █████  ███             ███ ███",
        "░░███ ░░███                        ░░███   ░███  ░░███  ░░░             ░███░███",
        " ░░███ ███    ██████  █████ ████    ░███   ░███   ░███  ████  ████████  ░███░███",
        "  ░░█████    ███░░███░░███ ░███     ░███   ░███   ░███ ░░███ ░░███░░███ ░███░███",
        "   ░░███    ░███ ░███ ░███ ░███     ░░███ █████ ████    ░███  ░███ ░███ ░███░███",
        "    ░███    ░███ ░███ ░███ ░███      ░░█████░█████░     ░███  ░███ ░███ ░░░ ░░░",
        "    █████   ░░██████  ░░████████      ░░███ ░░███      █████ ████ █████ ███ ███",
        "   ░░░░░     ░░░░░░    ░░░░░░░░         ░░░   ░░░      ░░░░░ ░░░░ ░░░░░ ░░░ ░░░"
    ]

    colors = [
        "#004d00",
        "#007300",
        "#009900",
        "#00cc00",
        "#00ff00",
        "#33ff33",
        "#66ff66",
        "#99ff99",
        "#66ff66",
        "#33ff33",
        "#00ff00",
        "#00cc00",
        "#009900",
        "#007300"
    ]

    animated_title(lines, colors, 0.035)


def lost():
    lines = [
        " █████ █████                        █████                         █████    ███ ███ ███",
        "░░███ ░░███                        ░░███                         ░░███    ░███░███░███",
        " ░░███ ███    ██████  █████ ████    ░███         ██████   █████  ███████  ░███░███░███",
        "  ░░█████    ███░░███░░███ ░███     ░███        ███░░███ ███░░  ░░░███░   ░███░███░███",
        "   ░░███    ░███ ░███ ░███ ░███     ░███       ░███ ░███░░█████   ░███    ░███░███░███",
        "    ░███    ░███ ░███ ░███ ░███     ░███      █░███ ░███ ░░░░███  ░███ ███░░░ ░░░ ░░░",
        "    █████   ░░██████  ░░████████    ███████████░░██████  ██████   ░░█████  ███ ███ ███",
        "   ░░░░░     ░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░  ░░░░░░     ░░░░░  ░░░ ░░░ ░░░"
    ]

    colors = [
        "#4a0000",
        "#730000",
        "#9c0000",
        "#c50000",
        "#ef0000",
        "#ff2a2a",
        "#ff5555",
        "#ff8080",
        "#ff5555",
        "#ff2a2a",
        "#ef0000",
        "#c50000",
        "#9c0000",
        "#730000"
    ]

    animated_title(lines, colors, 0.06)