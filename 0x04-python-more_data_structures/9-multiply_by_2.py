#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    new_value = []
    for key, value in a_dictionary.items():
        new_value.append(value*2)
        for i in new_value:
            new_dictionary[key] = i

    return (new_dictionary)
