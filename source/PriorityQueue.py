from abc import ABC, abstractmethod


class PriorityQueue(ABC):
    @abstractmethod
    def insert(self, key):
        pass

    @abstractmethod
    def findMin(self):
        pass

    @abstractmethod
    def deleteMin(self):
        pass

    @abstractmethod
    def decreaseKey(self, key):
        pass
