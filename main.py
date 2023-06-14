# Main gameplay file
from player import *
from enemy import *


def ActionMenu():
    print('Action Menu')
    print('------------')
    print('1 - Attack')
    print('2 - Defend')


print('Welcome to World of Pycraft')
# player_name = input(
#    'Enter your character name or select your character (character save files in progress): ')
# print(f"Hello {player_name}!")
player = Player('Test', 5, 5, 5, 10, 1, 0, 0)
max_hp = player.stam * 5
hp = max_hp

while hp > 0:
    # Level player up
    if player.xp >= 100:
        player.level_up()

    print('Your first enemy is a goblin')
    goblin = Enemy('Goblin', 10, 2)
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
        if goblin.hp < 0:
            print('Goblin Killed! You gain 5xp')
            player.xp += 10
    x = input('Press 1 to continue your journey: ')
