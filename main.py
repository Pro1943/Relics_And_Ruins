#    ▄▄▄▄▄▄▄         ▄▄                                  ▄▄   ▄▄▄▄▄▄▄                         
#    ███▀▀███▄       ██ ▀▀                               ██   ███▀▀███▄       ▀▀              
#    ███▄▄███▀ ▄█▀█▄ ██ ██  ▄████ ▄█▀▀▀    ▀▀█▄ ████▄ ▄████   ███▄▄███▀ ██ ██ ██  ████▄ ▄█▀▀▀ 
#    ███▀▀██▄  ██▄█▀ ██ ██  ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ███▀▀██▄  ██ ██ ██  ██ ██ ▀███▄ 
#    ███  ▀███ ▀█▄▄▄ ██ ██▄ ▀████ ▄▄▄█▀   ▀█▄██ ██ ██ ▀████   ███  ▀███ ▀██▀█ ██▄ ██ ██ ▄▄▄█▀ 

import os
import time
import json
import pathlib as pl
import prompt_toolkit as pt
from scenes import cmd
from scenes import main_scenes as ms
from functions import save_load as sl

folder_path=pl.Path("Relics-and-Ruins")
config = {
    "Initialized": True,
    "Version": "0.01.DEV"
}
initial = {

}
def initial_prep():
    (folder_path/"assets").mkdir(parents=True, exist_ok=True)
    with open("Relics-and-Ruins/assets/config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
    try:
        return sl.load("Initialized")  
    except FileNotFoundError:
        with open("Relics-and-Ruins/save.json", "w", encoding="utf-8") as s:
            json.dump(initial, s, indent=4)
        sl.save("Initialized", True)
        sl.save("Player_hp", 100)
        with open("Relics-and-Ruins/assets/enemy.json", "w", encoding="utf-8") as e:
            json.dump(enemy_index, e, indent=4)
        return "Initial Files Created"
def main():
    cmd.console_config(756,400)
    ms.titel()
    print(initial_prep())
    time.sleep(3)
if __name__ == "__main__":
    main()