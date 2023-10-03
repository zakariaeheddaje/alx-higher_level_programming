#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_number = (
    str(number)[len(str(number)) - 1]
    if number >= 0
    else "-" + str(number)[len(str(number)) - 1]
)

result = (
    "and is greater than 5"
    if int(last_number) > 5
    else ("and is 0" if int(last_number) == 0
          else "and is less than 6 and not 0")
)

print(f"Last digit of {number} is {last_number} {result}")
