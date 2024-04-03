#!/usr/bin/python
"""
URF_8 validation
"""


def validUTF8(data):
    """
    validates for UTF characters
    """
    bytes_for_following = 0

    for byte in data:
        if bytes_for_following == 0:
            if byte >> 5 == 0b110:
                bytes_for_following = 1
            elif byte >> 4 == 0b1110:
                bytes_for_following = 2
            elif byte >> 3 == 0b11110:
                bytes_for_following = 3
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_for_following -= 1
    return True
