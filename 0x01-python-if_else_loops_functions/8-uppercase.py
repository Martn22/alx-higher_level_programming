#!/usr/bin/python3

# This function prints a string in uppercase
def uppercase(str):
    result = ''
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            result = ord(x) - 32
            print(f"{chr(result)}")

        else:
            print(x)
