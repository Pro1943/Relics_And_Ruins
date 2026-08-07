from logic import player as pl
from logic import enemy as en

def enemy(id):
    name, hp, enemy_type, defense, attack, loot, description = en.spawn_enemy(id)
    return name, hp, enemy_type, defense, attack, loot, description
