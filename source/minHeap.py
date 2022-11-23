from source.priorityQueue import PriorityQueue


class MinHeap(PriorityQueue):
    def insert(self, key):
        print("MinHeap insert({})".format(key))

    def findMin(self):
        print("MinHeap findMin()")

    def deleteMin(self):
        print("MinHeap deleteMin()")

    def decreaseKey(self, key):
        print("MinHeap decreaseKey({})".format(key))
