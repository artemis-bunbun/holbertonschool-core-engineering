#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

ld = number - (10 * int(number / 10))

if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
if ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
if ld < 6:
    if ld != 0:
        print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
