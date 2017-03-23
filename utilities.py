import random
import os
import time

def roll(num, dicesize):
    total = []
    for i in range(num):
        roll = random.randint(1, dicesize)
        total.append(roll)
        total.sort()

    total.pop()
    return sum(total)
