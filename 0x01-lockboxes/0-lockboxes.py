#!/usr/bin/python3
"""
Module 0-lockboxes

This module contains a method to determine if all the lockboxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all the lockboxes can be opened.

    Args:
        boxes (list): A list of lists representing the lockboxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    opened_boxes = set()
    opened_boxes.add(0)

    keys = set(boxes[0])

    while keys:
        key = keys.pop()

        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])

    return len(opened_boxes) == len(boxes)
