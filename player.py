import random

"""
Player class checklist / markup

- Each player starts with 5 str, 5 dex, 5 int, 10 stam
- Level up gives player 3 skill points to allocate
- 6 inventory slots (Last)
    - Weapon
    - Hat
    - Chest
    - Gloves
    - Boots
    - Ring

"""


class Player:
    def __init__(self, name, str, dex, int, stam, level, xp, sp):
        self.name = name
        self.str = str
        self.dex = dex
        self.int = int
        self.stam = stam
        self.level = level
        self.xp = xp
        self.sp = sp

    def get_stats(self):
        print('Stats for ', self.name)
        print('STR =', self.str)
        print('DEX =', self.dex)
        print('INT =', self.int)
        print('STM =', self.stam)
        print('EXP = ', self.xp)
        print('Skill points = ', self.xp)

    def level_up(self):
        if self.xp >= 100:
            print('Level up!')
            self.xp = 0
            self.sp += 3
        while self.sp > 0:
            print('Current Stats: STR =', self.str,
                  'DEX =', self.dex,  'INT =', self.int)
            print('STM =', self.stam,  'XP=',
                  self.xp,  'Skill points =', self.sp)
            sel = input('Spend points, 1 = str, 2 = dex, 3 = int, 4 = stam')
            if sel == '1':
                self.str += 1
                self.sp -= 1
            elif sel == '2':
                self.dex += 1
                self.sp -= 1
            elif sel == '3':
                self.int += 1
                self.sp -= 1
            elif sel == '4':
                self.stam += 1
                self.sp -= 1

    def attack(self):
        dmg = round(random.uniform(self.str/2, self.str))
        crit_chance = round(random.uniform(0, 100), 2)
        if crit_chance < (self.dex / 2):
            print('Critical Strike!')
            dmg = dmg * 2
        return dmg
