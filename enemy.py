# File containing enemy classes and methods
import random


class Enemy:
    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str

    def attack(self):
        dmg = round(random.uniform(self.str/2, self.str))
        crit_chance = round(random.uniform(0, 100), 2)
        if crit_chance > 90:
            print('Critical Strike!')
            dmg = dmg * 2
        return dmg


Goblin = Enemy('Goblin', 10, 2)
print(Goblin.attack())
