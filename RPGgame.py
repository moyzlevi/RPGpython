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
battle = True
while battle is True:
    enemies.enemy1(35, 1, 1, True)
    battle = enemies.enemy1sys(i, x, y, z)

print("Congrats! You've passed the tutorial. Now press Enter to continue...")
