class Dijkstra():
    def run(self, graph, PriorityQueue):
        print("Dijkstra run(nodes={}, edges={})".format(len(graph.nodes), len(graph.edges)))
        priorityQueue = PriorityQueue()
        for v in graph.nodes:
            priorityQueue.insert(v)
