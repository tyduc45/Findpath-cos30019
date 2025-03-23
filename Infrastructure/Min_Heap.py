# Min_Heap.py -- Custom Min Heap Implementation
# ----------------------------------------------------------------------------------------
# This module provides a custom implementation of MinHeap,
# which is used as a priority queue for the A* search algorithm.
#
# Implemented Functions:
# 1. `push(item)`: Inserts a new element while maintaining heap order.
# 2. `pop()`: Removes and returns the smallest element (root).
# 3. `heapify_up(index)`: Moves an inserted element upwards to maintain heap property.
# 4. `heapify_down(index)`: Moves the root element downwards after removal.
# 5. `peek()`: Returns the smallest element without removing it.
# 6. `__len__()`: Returns the number of elements in the heap.
#
# This heap is primarily designed for A* search, where elements are stored as
# `(f(n), node, path)`, ensuring that nodes with the lowest cost are expanded first.
# ----------------------------------------------------------------------------------------
# Written by Yifan Li / Xiaonan Li
# Date: 20/03/2025
#

class MinHeap:
    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Maintain heap property from bottom to top
    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:  # Compare f(n)
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Swap
            index = parent
            parent = (index - 1) // 2

    # Insert a new item into the heap
    def push(self, item):
        self.heap.append(item)  # Append to the end
        self.heapify_up(len(self.heap) - 1)  # Fix heap property

    # Remove and return the smallest element (root)
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element

        root = self.heap[0]  # Root element (min)
        self.heap[0] = self.heap.pop()  # Move last element to root
        self.heapify_down(0)  # Fix heap property
        return root

    # Return the smallest element without removing it
    def peek(self):
        return self.heap[0] if self.heap else None

    # Maintain heap property from top to bottom
    def heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1  # Left child
            right = 2 * index + 2  # Right child
            smallest = index

            # Compare with left child
            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            # Compare with right child
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break  # No swap needed, heap property restored

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    # Return the number of elements in the heap
    def __len__(self):
        return len(self.heap)