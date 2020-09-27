"""
Python Game
"""
import os
import random
import enemies
import storycode
import sys


# game variables

dif = -1

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
#dif = storycode.intro()
enemies.enemy1()


i = input()
cls()
x = 0
y = 0
z = 0

# enemy1 tutorial battle:

enemies.enemy1(35, 1, 1, True)
while i is not None:
    op = -1
    life = 10
    op = int(input())
    if x == 0 and y == 0 and z == 0:
        lista = enemies.enemy1()
    else:
        lista = enemies.enemy1(x, y, z)
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
        print("You took "+str(w)+" of damage!")
        input()
    elif w == 2:
        life -= w
        print("Ragout Rabbit attacked:")
        print("It was a critical attack!")
        print("You took " + str(w) + " of damage!")
        input()
    else:
        print("Ragout Rabbit missed the attack")
        input()
    cls()
    y = 2 * rng
    cls()
    x = enemies.enemy1(x, y, z, True, op, life)[0]
    # Dead text
    if x <= 0:
        cls()
        print("Ragout Rabbit died")
        break
