#!/usr/bin/python3

"""This code is a function that trys to unlock locked boxes."""
def canUnlockAll(boxes):
    """This is a function that tries to unlock locked boxes."""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key < n and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)

    return all(unlocked)
