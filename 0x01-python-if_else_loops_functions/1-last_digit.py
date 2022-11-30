#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = -(number)
    #turn number into positive
else:
    num = number

last_digit = num % 10
if last_digit > 5:
    assign = "and is greater than 5"
elif last_digit == 0:
    assign = "and is 0"
elif last_digit < 6 and last_digit > 0:
    assign = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {assign}")
