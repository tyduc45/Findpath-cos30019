class MinHeap:
    def __init__(self):
        self.data = []                  # empty datalist for heap


    def swap(self,i,j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def heapify_up(self,index):         # recover heap from bottom to top
        parent = (index - 1) // 2
        while index > 0 and self.data[index] > self.data[parent]:
            self.swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self,index):       # recover heap from bottom to top
        n = len(self.data) - 1
        smallest = index

        while True:
            left = index * 2 + 1
            right = index * 2 + 2

            # compare to the left
            if left < n and self.data[smallest][0] > self.data[left][0]:
                smallest = left

            # compare to the right
            if right < n and self.data[smallest][0] > self.data[right][0]:
                smallest = right

            # if no more changes on the index , we stop
            if smallest == index:
                break

            #
            self.swap(index, smallest)
            index = smallest



    def push(self,item):               # append new item
        self.data.append(item)
        self.heapify_up(len(self.data)-1)

    def pop(self):                     # delete from it
        if not self.data:
            return None

        self.swap(0, len(self.data)-1)    # list.pop() is set to pop the last one by default
        item = self.data.pop()
        self.heapify_down(0)                # recover heap from top
        return item                         # return the remove item

    def peek(self):
        if not self.data:
            return None
        return self.data[0]


