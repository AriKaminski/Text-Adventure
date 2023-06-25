# File containing enemy classes and methods
import random


class Enemy:
    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str

    def take_damage(self, dmg):
        self.hp -= dmg


class Goblin(Enemy):
    def __init__(self, name, hp, str):
        super().__init__(name, hp, str)

    def attack(self):
        dmg = round(random.uniform(self.str/2, self.str))
        return dmg

    # def take_damage(self, dmg):
        # self.hp -= dmg


class Bandit(Enemy):
    def __init__(self, name, hp, str):
        super().__init__(name, hp, str)

    def attack(self):
        dmg = round(random.uniform(self.str/2, self.str))
        crit_chance = round(random.uniform(0, 100), 2)
        if crit_chance > 90:
            print('Critical Strike!')
            dmg = dmg * 2
        return dmg


class Skeleton(Enemy):
    def __init__(self, name, hp, str):
        super().__init__(name, hp, str)


bandit = Bandit('Bandit', 15, 2)


goblin = Goblin('Goblin', 10, 2)
# print(bandit.hp)


"""
def easyEnemies():
    goblin = Enemy('Goblin', 10, 4)
    bandit = Bandit('Bandit', 15, 3)
    enemyList = [goblin, bandit]
    choice = random.choice(enemyList)
    return choice
"""
