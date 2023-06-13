# Main gameplay file
from player import *
from enemy import *


class ActionMenu():
    print('Action Menu')
    print('------------')
    print('1 - Attack')
    print('2 - Defend')


print('Welcome to World of Pycraft')
# player_name = input(
#    'Enter your character name or select your character (character save files in progress): ')
# print(f"Hello {player_name}!")
player = Player('Test', 5, 5, 5, 10, 1, 0, 0)
goblin = Enemy('Goblin', 10, 2)
max_hp = player.stam * 5
hp = max_hp

while hp > 0:
    print('Your first enemy is a goblin')
    while goblin.hp > 0:
        ActionMenu()
        action = input('Select an action: ')
        if action == '1':
            dmg = player.attack()
            print(f"You deal {dmg} damage")
            goblin.take_damage(dmg)
            print(f"Goblin hp = {goblin.hp}")
        elif action == '2':
            pass
