from functions import save_load as sl
from rich.console import Console
from rich.align import Align
from rich.live import Live
from rich.text import Text
from rich.table import Table
from logic.player import *
console = Console()

def spawn_enemy(id):
    enemy = sl.load("assets/enemy_index.json", id)
    if enemy is None:
        console.print(f"Enemy with ID {id} not found.", style="bold red")
        return None
    return enemy

def fight(enemy_id):
    enemy = spawn_enemy(enemy_id)
    if enemy is None:
        return None

    console.print(
        f"You Encountered a {enemy['name']}",
        style="bold yellow",
        justify="center"
    )
    console.print()
    table = Table.grid(expand=True, padding=(0, 0))
    table.add_column(justify="left", ratio=1)
    table.add_column(justify="right", ratio=1)
    table.add_row(
        Text(f"Enemy HP: {enemy['hp']}", style="bold red"),
        Text(f"Enemy Type: {enemy['type']}", style="bold blue")
    )
    console.print(table)
    console.print("\n\n")

    console.print(
        f"Your HP: {get_player_hp()}",
        style="bold green",
        justify="left"
    )