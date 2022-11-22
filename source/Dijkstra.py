class Dijkstra():
    def run(self, graph, source, PriorityQueue):
        print("Dijkstra run({})".format(source))
        priorityQueue = PriorityQueue()
        priorityQueue.insert(source)
