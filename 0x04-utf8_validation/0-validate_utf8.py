#!/usr/bin/python
"""
URF_8 validation
"""


def validUTF8(data):
    """
    validates for UTF characters
    params:
        data which is a list of integers
    return:
        True if valid Utf
    """
    bytes_for_following = 0

    for byte in data:
        if bytes_for_following == 0:
            if byte >> 5 == 0b110:  # 2byte
                bytes_for_following = 1
            elif byte >> 4 == 0b1110:  # 3byte
                bytes_for_following = 2
            elif byte >> 3 == 0b11110:  # 4 byte
                bytes_for_following = 3
        else:
            if byte >> 6 != 0b10:  # check for next item in list
                return False
            bytes_for_following -= 1
            
    return True
