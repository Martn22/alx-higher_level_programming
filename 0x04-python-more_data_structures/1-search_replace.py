#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for i in range(len(new_list)):
        if search in new_list:
            new_list[i] = replace
        else:
            new_list[i]

    return (new_list)
