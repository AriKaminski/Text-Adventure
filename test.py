import random
from player import *
from enemy import *


def easyEnemies():
    goblin = Enemy('Goblin', 10, 4)
    bandit = Bandit('Bandit', 15, 3)
    enemyList = [goblin, bandit]
    choice = random.choice(enemyList)
    return choice


current_enemy = easyEnemies()
print(current_enemy.name, current_enemy.hp)
