
def ActionMenu():
    print('Action Menu')
    print('------------')
    print('1 - Attack')
    print('2 - Defend')


def TownMenu():
    town_dict = {
        1: "Market Square",
        2: "Castle Keep",
        3: "Tavern",
        4: "Merchant's Guild",
        5: "Elwynn Forest"
    }
    for town in town_dict:
        print(town, town_dict[town])


TownMenu()
