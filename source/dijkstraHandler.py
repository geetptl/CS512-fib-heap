import random

import matplotlib.pyplot as plt
import networkx as nx

from source.dijkstra import Dijkstra


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
            dijkstra.run(graph, PriorityQueue)
