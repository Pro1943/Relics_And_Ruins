import os
import json

enemy_index = {
    "001": {
        "name": "Caveman",
        "hp": 50,
        "type": "Monster",
        "attack":{
            "club_smash":{
                "name": "Club Smash",
                "damage": 10,
                "accuracy": 0.8,
                "description": "A powerful swing of a wooden club.",
                "weight": 0.70
            },
            "stone_throw":{
                "name": "Stone Throw",
                "damage": 5,
                "accuracy": 0.6,
                "description": "Throws a small stone at the player.",
                "weight": 0.29
            },
            "club_throw":{
                "name": "Club Throw",
                "damage": 25,
                "accuracy": 0.4,
                "description": "Throws a heavy wooden club at the player.",
                "weight": 0.01
            }

        },
        "defense": 5,
        "loot": {
            "000":{
                "name": "XP",
                "amount": 15
            }
        },
        "description": "A primitive human wielding a club, ready to attack."
    },
    "002": {
        "name": "Zombie",
        "hp": 80,
        "type": "Undead",
        "attack":{
            "zombie_bite":{
                "name": "Zombie Bite",
                "damage": 15,
                "accuracy": 0.7,
                "description": "A vicious bite from the undead.",
                "weight": 0.8
            },
            "zombie_scratch":{
                "name": "Zombie Scratch",
                "damage": 10,
                "accuracy": 0.9,
                "description": "A scratch from the undead.",
                "weight": 0.2
            }
    },
    "defense": 3,
    "loot": {
        "000":{
            "name": "XP",
            "amount": 20
        }
    },
    "description": "A reanimated corpse that craves human flesh."
    }
}