# Itertools.py - Custom Implementation of itertools.count()
# ----------------------------------------------------------------------------------------
# This module provides a custom implementation of `itertools.count()`.
# The `count()` function generates an infinite sequence of numbers, starting from 0,
# and increasing by 1 each time `next()` is called.
#
# Used in A* search algorithm as a tie-breaker to ensure that when multiple paths
# have the same cost, the one that was inserted first gets expanded first.
# ----------------------------------------------------------------------------------------
# Written by Xiaonan Li, 105206175
# Date: 23/03/2025
#

class Counter:
    # Custom counter class to replace itertools.count()

    def __init__(self):
        # Initialize the counter starting at 0
        self.value = 0

    def next(self):
        # Returns the current count and increments the counter
        self.value += 1
        return self.value - 1