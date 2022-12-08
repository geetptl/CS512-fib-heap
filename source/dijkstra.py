import time

class Dijkstra():
    def update(dist, pred, u, v):
        if dist[u] + path_weight(graph, [u,v]) < dist[v]:
            dist[v] = dist[u] + nx.path_weight(graph, [u,v])
            pred[v] = u
        return dist, pred
    
    def dijkstra(source):
        dist = []
        pred = []
        for node in nodes(graph):
            dist[node] = 10000
            pred[node] = None
            priorityQueue.insert(node)
        dist[source] = 0

        while len(minheap) != 0:
            u = priorityQueue.deleteMin()
            for v in neighbors(graph, u):
                dist, pred = update(dist, pred, u, v)

        return dist, pred

    def run(self, graph, PriorityQueue):
        result_dist = []
        result_pred = []
        print("Dijkstra run(nodes={}, edges={})".format(len(graph.nodes), len(graph.edges)))
        priorityQueue = PriorityQueue()
        start_time = time.time()
        for v in graph.nodes:
            dist, pred = dijkstra(v)
            result_dist[v] = dist
            result_pred[v] = pred
        print("--- %s seconds ---" % (time.time() - start_time))





            

