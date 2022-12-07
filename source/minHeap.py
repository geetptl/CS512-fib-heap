from source.priorityQueue import PriorityQueue

class MinHeap(PriorityQueue):
    def __init__(self):
        self.elements = []
        self.size = 0

    def insert(self, key):
        self.elements.append(key)
        self.size+=1
        self.heapifyUpwards(self.size-1)
        return 
        # print("MinHeap insert({})".format(key))

    def findMin(self):
        return self.elements[0]
        #print("MinHeap findMin()")

    def deleteMin(self):
        k = self.elements[0]
        self.elements[0] = self.elements[-1]
        del self.elements[-1]
        self.size-=1
        self.heapifyDownwards(0)
        return k
        #print("MinHeap deleteMin()")
    
    def heapifyUpwards(self, i):
        while i != 0:
            p = (i - 1) // 2
            if self.elements[i][0] < self.elements[p][0]:
                self.elements[i], self.elements[p] = self.elements[p], self.elements[i]
            i = p
    
    def heapifyDownwards(self, i):
        while i < self.size:
            if 2 * (i + 1) >= self.size:
                m = (2 * i) + 1
            else:
                m = (2 * i) + 1 if self.elements[(2 * i) + 1][0] < self.elements[2 * (i + 1)][0] else 2 * (i + 1)
            if m>=self.size:
                break
            if self.elements[m][0] < self.elements[i][0]:
                self.elements[i], self.elements[m] = self.elements[m], self.elements[i]
            i = m
