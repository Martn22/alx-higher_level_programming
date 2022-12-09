#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    if search in new_list:
        for i in new_list:
            new_list[i] = replace
    
    return (new_list)
