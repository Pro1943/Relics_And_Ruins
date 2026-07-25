#    ▄▄▄▄▄▄▄         ▄▄                                  ▄▄   ▄▄▄▄▄▄▄                         
#    ███▀▀███▄       ██ ▀▀                               ██   ███▀▀███▄       ▀▀              
#    ███▄▄███▀ ▄█▀█▄ ██ ██  ▄████ ▄█▀▀▀    ▀▀█▄ ████▄ ▄████   ███▄▄███▀ ██ ██ ██  ████▄ ▄█▀▀▀ 
#    ███▀▀██▄  ██▄█▀ ██ ██  ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ███▀▀██▄  ██ ██ ██  ██ ██ ▀███▄ 
#    ███  ▀███ ▀█▄▄▄ ██ ██▄ ▀████ ▄▄▄█▀   ▀█▄██ ██ ██ ▀████   ███  ▀███ ▀██▀█ ██▄ ██ ██ ▄▄▄█▀ 

import os
import pathlib as pl
import json
import prompt_toolkit as pt
from scenes import main_scenes as ms
from scenes import cmd
import time
folder_path=pl.Path("Relics-and-Ruins")
config = {
    "Initialized": True,
    "Version": "0.01.DEV"
}

def initial_prep():
    (folder_path/"assets").mkdir(parents=True, exist_ok=True)
    with open("Relics-and-Ruins/assets/config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
    
def main():
    cmd.console_config(756,400)
    ms.titel()
    initial_prep()
    time.sleep(10)
if __name__ == "__main__":
    main()