import random

import matplotlib.pyplot as plt
import networkx as nx

from source.dijkstra import Dijkstra
from source.fibHeap import FibHeap
from source.minHeap import MinHeap


def isEqual(m_dist, f_dist, graph):
    for n in graph.nodes:
        for m in graph.nodes:
            if m_dist[n][m] != f_dist[n][m]:
                return False
    return True


class DijkstraHandler:

    @classmethod
    def run(cls, nodes, edges, runs, PriorityQueue, priorityQueueType):
        for i in range(0, runs):
            print("Run {}".format(i + 1))
            graph = nx.gnm_random_graph(nodes, edges, seed=None, directed=False)
            weightedEdges = []
            for e in graph.edges:
                weightedEdges.append((e[0], e[1], random.randint(a=0, b=100)))
                graph.remove_edge(e[0], e[1])
            graph.add_weighted_edges_from(weightedEdges)
            pos = nx.drawing.spring_layout(graph)
            nx.draw(graph, pos, with_labels=True)
            edge_labels = nx.get_edge_attributes(graph, "weight")
            nx.draw_networkx_edge_labels(graph, pos, edge_labels)
            plt.savefig("outputs/n_{}_e_{}_pq_{}_run_{}.png".format(nodes, edges, priorityQueueType, i))
            plt.figure().clear()
            dijkstra = Dijkstra()
            if PriorityQueue is None:
                m_time, m_dist, m_pred = dijkstra.run(graph, MinHeap)
                f_time, f_dist, f_pred = dijkstra.run(graph, FibHeap)
                print(isEqual(m_dist, f_dist, graph))
                print("Minheap time", m_time)
                print("Fibheap time", f_time)
            else:
                dijkstra.run(graph, PriorityQueue)
