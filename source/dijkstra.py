import math
import time


def dijkstra(graph, source, PriorityQueue):
    dist = {}
    pred = {}
    priorityQueue = PriorityQueue()
    for node in graph.nodes:
        dist[node] = math.inf
        pred[node] = None
    dist[source] = 0
    priorityQueue.insert((dist[source], source))

    while priorityQueue.length() != 0:
        u = priorityQueue.deleteMin()[1]
        for v in graph[u]:
            if dist[u] + graph[u][v]['weight'] < dist[v]:
                dist[v] = dist[u] + graph[u][v]['weight']
                pred[v] = u
                priorityQueue.insert((dist[v], v))
    return dist, pred


class Dijkstra():
    def run(self, graph, PriorityQueue):
        result_dist = {}
        result_pred = {}
        print("Dijkstra run(nodes={}, edges={})".format(len(graph.nodes), len(graph.edges)))
        start_time = time.time()
        for v in graph.nodes:
            dist, pred = dijkstra(graph, v, PriorityQueue)
            result_dist[v] = dist
            result_pred[v] = pred
        return time.time() - start_time, result_dist, result_pred
