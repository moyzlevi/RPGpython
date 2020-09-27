"""
Script that contains the story code
"""


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    nerveGear = CYAN + "Nerve Gear" + END
    swo = CYAN + "Sword Art Online" + END
    attackString = RED + "Attack" + END
    defenseString = GREEN + "Defense" + END
    skillString = YELLOW + "Skill" + END


def intro():
    # start intro
    print('Hello, welcome to the world of Sword Art Online')
    input("Press Enter to continue...")
    input()
    print('In this world, you will learn to survive to different challenges')
    print('Please, choose a difficult level:')
    print('Choose a number : easy-0, medium-1, hard-2')

    dif = int(input())
    while dif is not None:
        if dif != 0 and dif != 1 and dif != 2:
            print('Insert a valid number')
            x = input()
            dif = int(x)
        if dif == 0 or dif == 1 or dif == 2:
            break
    if dif == 2:
        print("You've chosen the hard mode")
    elif dif == 1:
        print("You've chosen the medium mode")
    else:
        print("You've chosen the easy(loser)")

    input()
    print(Color.swo + " it's a game of VRMMORPG, it uses " + Color.nerveGear
          + " that inserts you into a virtual reality")
    input()
    print(
        "Your first objective is to pass the tutorial. "
        "In this game, there are three types of action: "
        + Color.attackString + ", " + Color.defenseString + " and " + Color.skillString)
    print("You can use the three actions on the next enemy")
    return dif
    # end intro
