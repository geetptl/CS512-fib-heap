from source import PriorityQueue


class FibHeap(PriorityQueue.PriorityQueue):
    def insert(self, key):
        print("FibHeap insert({})".format(key))

    def findMin(self):
        print("FibHeap findMin()")

    def deleteMin(self):
        print("FibHeap deleteMin()")

    def decreaseKey(self, key):
        print("FibHeap decreaseKey({})".format(key))
