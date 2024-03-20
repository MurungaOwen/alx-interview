#!/usr/bin/python3
"""module containing min_operation"""


def minOperations(n: float) -> int:
    """get minimum operations
    params:
        n representing the number
    return
        sum of min operations
    """
    divisor = 2
    list = []
    while n > 1:
        while n % divisor == 0:
            list.append(divisor) 
            n = n / divisor
        divisor += 1
    minimum = sum(list)
    return minimum
