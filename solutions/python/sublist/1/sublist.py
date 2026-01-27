"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'


def sublist(list_one, list_two):
    n, m = len(list_one), len(list_two)
    if list_one == list_two:
        return EQUAL
    if n ==0:
        return SUBLIST
    if m == 0:
        return SUPERLIST
    if n > m:
        for i in range(n - m +1):
            if list_one[i:i+m] == list_two:
                return SUPERLIST
    if m > n:
        for i in range(m - n+ 1):
            if list_two[i:i+n] == list_one:
                return SUBLIST
    return UNEQUAL
        

    


