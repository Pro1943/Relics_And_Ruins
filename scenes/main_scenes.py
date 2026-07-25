from rich.console import Console
from rich.align import Align

console = Console()

def center_print(text: str, style: str):
    console.print(Align.center(text, style=style))

def titel():
    center_print("  ▄▄▄▄▄▄         ▄▄                                        ▄▄▄▄▄▄                        ", style="bold #00FFFF")
    center_print(" █▀██▀▀▀█▄        ██                                 █▄   █▀██▀▀▀█▄                      ", style="bold #00FFFF")
    center_print("   ██▄▄▄█▀        ██ ▀▀                     ▄        ██     ██▄▄▄█▀        ▀▀ ▄          ", style="bold #0000FF")
    center_print("   ██▀▀█▄   ▄█▀█▄ ██ ██ ▄███▀ ▄██▀█   ▄▀▀█▄ ████▄ ▄████     ██▀▀█▄   ██ ██ ██ ████▄ ▄██▀█", style="bold #0000FF")
    center_print(" ▄ ██  ██   ██▄█▀ ██ ██ ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ▄ ██  ██   ██ ██ ██ ██ ██ ▀███▄", style="bold #00BFFF")
    center_print(" ▀██▀  ▀██▀▄▀█▄▄▄▄██▄██▄▀███▄█▄▄██▀  ▄▀█▄██▄██ ▀█▄█▀███   ▀██▀  ▀██▀▄▀██▀█▄██▄██▄▀██▄▄██▀", style="bold #00BFFF")

def victory():
    center_print(" █████ █████                        █████   ███   █████  ███             ███ ███", style="bold #008000")
    center_print("░░███ ░░███                        ░░███   ░███  ░░███  ░░░             ░███░███", style="bold #008000")
    center_print(" ░░███ ███    ██████  █████ ████    ░███   ░███   ░███  ████  ████████  ░███░███", style="bold #00FF00")
    center_print("  ░░█████    ███░░███░░███ ░███     ░███   ░███   ░███ ░░███ ░░███░░███ ░███░███", style="bold #00FF00")
    center_print("   ░░███    ░███ ░███ ░███ ░███     ░░███  █████  ███   ░███  ░███ ░███ ░███░███", style="bold #00FF7F")
    center_print("    ░███    ░███ ░███ ░███ ░███      ░░░█████░█████░    ░███  ░███ ░███ ░░░ ░░░ ", style="bold #00FF7F")
    center_print("    █████   ░░██████  ░░████████       ░░███ ░░███      █████ ████ █████ ███ ███", style="bold #00CD66")
    center_print("   ░░░░░     ░░░░░░    ░░░░░░░░         ░░░   ░░░      ░░░░░ ░░░░ ░░░░░ ░░░ ░░░ ", style="bold #00CD66")

def lost():
    center_print(" █████ █████                        █████                         █████    ███ ███ ███", style="bold #FF0000")
    center_print("░░███ ░░███                        ░░███                         ░░███    ░███░███░███", style="bold #FF0000")
    center_print(" ░░███ ███    ██████  █████ ████    ░███         ██████   █████  ███████  ░███░███░███", style="bold #8B0000")
    center_print("  ░░█████    ███░░███░░███ ░███     ░███        ███░░███ ███░░  ░░░███░   ░███░███░███", style="bold #8B0000")
    center_print("   ░░███    ░███ ░███ ░███ ░███     ░███       ░███ ░███░░█████   ░███    ░███░███░███", style="bold #DC143C")
    center_print("    ░███    ░███ ░███ ░███ ░███     ░███      █░███ ░███ ░░░░███  ░███ ███░░░ ░░░ ░░░ ", style="bold #DC143C")
    center_print("    █████   ░░██████  ░░████████    ███████████░░██████  ██████   ░░█████  ███ ███ ███", style="bold #B22222")
    center_print("   ░░░░░     ░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░  ░░░░░░     ░░░░░  ░░░ ░░░ ░░░ ", style="bold #B22222")
