#!/usr/bin/python3
"""
Main file for making change
"""


def makeChange(coins, total):
    """
    get the change given coins as list of coins
    and total as the amount we need to reach
    """
    if total <= 0:
        return 0
    else:
        new_array = sorted(coins)
        size = len(new_array)
        answer = []
        while (size - 1) >= 0:
            while total >= new_array[size-1]:
                total -= new_array[size-1]
                answer.append(new_array[size-1])
            size -= 1
        if total == 0:
            # if we cant subtract and we have nothing remaining
            return len(answer)
        return -1
