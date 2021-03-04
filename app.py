#!usr/bin/env python3

import sys

ERR_NUM_ARGS = 'Exactly 3 numbers are required'
ERR_NON_NUMERIC = 'All inputs must be numeric'
TEEN_RANGE = range(13, 20)
UNACCEPTABLE_TEENS = (15, 16)

args = sys.argv[1:]


def special_sum(args=[]):
    """
    Stop execution and if arguments passed are
    not equal to 3
    print error message if not the case
    """
    if len(args) != 3:
        print(ERR_NUM_ARGS)
        return

    num_list = []

    """
    coerce the numeric type of string and add to
    num_list
    print error message if wrong type is provided
    """
    for arg in args:
        if type(arg) == int or arg.isnumeric():
            num_list.append(int(arg))
        else:
            print(ERR_NON_NUMERIC)
            return

    sum = 0

    """
    sum of all numbers in num list
    where numbers from 13 to 19 should be treated as 0
    except numbers 15 and 16
    """
    for num in num_list:
        if num in TEEN_RANGE and num not in UNACCEPTABLE_TEENS:
            num = 0
        sum += num

    print(sum)


if __name__ == '__main__':
    special_sum(args)
