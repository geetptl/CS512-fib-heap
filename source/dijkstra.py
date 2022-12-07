class Dijkstra():
    def run(self, graph, PriorityQueue):
        # How to access edge weights:
        # for u, v, d in graph.edges(data=True):
        #     print(d['weight'])
        print("Dijkstra run(nodes={}, edges={})".format(len(graph.nodes), len(graph.edges)))
        priorityQueue = PriorityQueue()
        for v in graph.nodes:
            priorityQueue.insert(v)
