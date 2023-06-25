
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
    print('TOWN MENU')
    print('===========================')
    for location in town_dict:
        print(location, town_dict[location])


def ForestMenu():
    forest_dict = {
        1: 'Redstone Cave',
        2: 'Bandit Circle',
        3: 'Duskwind Bridge',
        4: 'Back to town'
    }

    for location in forest_dict:
        print(location, forest_dict[location])


TownMenu()
