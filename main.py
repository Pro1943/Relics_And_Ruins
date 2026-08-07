#    ▄▄▄▄▄▄▄         ▄▄                                  ▄▄   ▄▄▄▄▄▄▄                         
#    ███▀▀███▄       ██ ▀▀                               ██   ███▀▀███▄       ▀▀              
#    ███▄▄███▀ ▄█▀█▄ ██ ██  ▄████ ▄█▀▀▀    ▀▀█▄ ████▄ ▄████   ███▄▄███▀ ██ ██ ██  ████▄ ▄█▀▀▀ 
#    ███▀▀██▄  ██▄█▀ ██ ██  ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ███▀▀██▄  ██ ██ ██  ██ ██ ▀███▄ 
#    ███  ▀███ ▀█▄▄▄ ██ ██▄ ▀████ ▄▄▄█▀   ▀█▄██ ██ ██ ▀████   ███  ▀███ ▀██▀█ ██▄ ██ ██ ▄▄▄█▀ 

import time
import json
import pathlib as pl
import prompt_toolkit as pt
from scenes import cmd
from scenes import main_scenes as ms
from scenes import static_screens as ss
from functions import save_load as sl
from charecters.enemies import enemy_index as ei

def initial_prep():
    sl.save("assets/config.json", "Initialized", True)
    sl.save("assets/config.json", "Version", "0.01.DEV")
    sl.save("assets/player/player.json", "Player_hp", 100)
    sl.save("assets/player/player.json", "Player_defence", 10)
    sl.save("assets/player/player.json", "Player_attack", 10)
    ei.save_enemy_index()

def main():
    if sl.load("assets/config.json", "Initialized") is None:
        initial_prep()
    cmd.console_config(800, 600)
    ms.title()
    cmd.clean_screen()
    ss.static_title()
    ms.center_print("Welcome to Relics and Ruins!", "bold #ad2df7")
    time.sleep(5)

if __name__ == "__main__":
    main()