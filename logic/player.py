from functions import save_load as sl

def get_player_hp():
    return sl.load("assets/player/player.json", "Player_hp")

def get_player_defence():
    return sl.load("assets/player/player.json", "Player_defence")

def get_player_attack():
    return sl.load("assets/player/player.json", "Player_attack")

def get_player_xp():
    return sl.load("assets/player/player.json", "Player_XP")