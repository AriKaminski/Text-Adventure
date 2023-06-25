# Main gameplay file
from player import *
from enemy import *
from Menus import *
import sys


print('Welcome to World of Pycraft')
# player_name = input(
#    'Enter your character name or select your character (character save files in progress): ')
# print(f"Hello {player_name}!")

# Create player object and set hp to max hp for gameplay
player = Player('Test', 5, 5, 5, 10, 1, 0, 0)
max_hp = player.stam * 5
hp = max_hp
print("You wake up in a medieval inn, greeted by the warmth of a crackling hearth and the aroma of a bustling morning.")
print("The innkeeper, intrigued by your arrival, offers you a map that holds the promise of adventure and destiny.")
print("With courage in your heart, you step into the vibrant world of Medieval Realms, ready to carve your own legend.")
print("The wind carries whispers of ancient quests and hidden treasures, urging you to take your first step.")
print()


# Town menu to decide where to go in town, possibly multiple towns?
TownMenu()

choice = input("What will it be? 9 to quit: ")
# Start game loop, I think user could just be prompted with town menu to go
if choice == '1':
    pass
    # Market code goes here
elif choice == '2':
    pass
    # Castle code goes here
elif choice == '3':
    pass
    # Tavern code goes here
elif choice == '4':
    pass
    # Tavern code goes here
elif choice == '5':
    ForestMenu()

elif choice == '9':
    sys.exit()


while hp > 0:
    # Level player up
    if player.xp >= 100:
        player.level_up()

    # Simple creation of Goblin enemy for battle testing. I think this could be done in a separate file?
    goblin = Goblin('Goblin', 10, 2)
    print(f'Your first enemy is a goblin with {goblin.hp} max hp')

    while goblin.hp > 0:
        ActionMenu()
        action = input('Select an action: ')
        if action == '1':
            dmg = player.attack()
            print(f"You deal {dmg} damage")
            goblin.take_damage(dmg)

        elif action == '2':
            dmg = goblin.attack()
            dmg = player.defend(dmg)
            hp -= dmg
            print('You defend!')

        dmg = goblin.attack()
        hp -= dmg

        print(f'You take {dmg} damage.')
        print(f"Your hp = {hp}| Goblin hp = {goblin.hp}")

        if goblin.hp < 0:
            print('Goblin Killed! You gain 10xp')
            player.xp += 10
            hp = max_hp
    x = input('Press 1 to continue your journey: ')
