from storycode import Color
import random


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
