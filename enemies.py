from storycode import Color
import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def enemy1sys(i=None, x=0, y=0, z=0):
    while i is not None:
        op = -1
        life = 10
        op = int(input())
        if x == 0 and y == 0 and z == 0:
            lista = enemy1()
        else:
            lista = enemy1(x, y, z)
        x = lista[0]  # rabbit's hp
        y = lista[1]  # player's attack
        z = lista[2]  # rabbit's defense
        w = lista[3]  # rabbit's attack dmg
        # rng system
        rng = random.randint(1, 101)
        if 5 <= rng <= 11:
            rng = 2
        elif 4 >= rng >= 2:
            rng = 3
        elif rng == 1:
            rng = 4
        else:
            rng = 1

        if rng != 1:
            print("Critical Attack: -" + str(2 * rng - 1))
            input()
        else:
            print("Attack Damage: -1")
            input()
        print()
        if w == 1:
            life -= w
            print("Ragout Rabbit attacked:")
            print("You took " + str(w) + " of damage!")
            input()
        elif w == 2:
            life -= w
            print("Ragout Rabbit attacked:")
            print("It was a critical attack!")
            print("You took " + str(w) + " of damage!")
            input()
            if life <= 0:
                print("You died!")
                input()
                cls()
                return
        else:
            print("Ragout Rabbit missed the attack")
            input()
        cls()
        y = 2 * rng
        cls()
        x = enemy1(x, y, z, True, op, life)[0]
        # Dead text
        if x <= 0:
            cls()
            print("Ragout Rabbit died")
            return False


def enemy1(hp=35, atck=2, df=1, pt=False, op=-1, life=10,):
    rng = random.randint(1, 101)
    if 95 <= rng <= 100:
        hostile_value = 2
    elif 80 <= rng <= 90:
        hostile_value = 1
    else:
        hostile_value = 0

    if op == int(0) and pt is not False:
        hp -= (atck - df)

    if pt:
        print("Ragout Rabbit")
        print("Life:" + str(hp))
        for p in range(0, hp):
            print("|", end='')
        print()
        print(r"""               ((`\ """)
        print(r"""            ___|| '--._ """)
        print(r"""         .'`   `'    o  )""")
        print(r"""        /    \   '. __.' """)
        print(r"""       _|    /_  \ \_\_  """)
        print(r"""      {_\______\-'\__\_\ """)
        print("Your life: " + str(life))
        print(Color.attackString + "-0  " + Color.defenseString + "-1 " + Color.skillString + "-2")

    return [hp, atck, df, hostile_value]
