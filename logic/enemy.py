from functions import save_load as sl

def spawn_enemy(id):
    enemy = sl.load("assets/enemy_index.json", id)
    name = enemy["name"]
    hp = enemy["hp"]
    enemy_type = enemy["type"]
    defense = enemy["defense"]
    attack = enemy["attack"]
    loot = enemy["loot"]
    description = enemy["description"]

    return name, hp, enemy_type, defense, attack, loot, description