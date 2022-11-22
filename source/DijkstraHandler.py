import matplotlib.pyplot as plt
import networkx as nx

from source import Dijkstra


class DijkstraHandler:
    @classmethod
    def run(cls, nodes, edges, runs, PriorityQueue, priorityQueueType):
        for i in range(0, runs):
            print("Run {}".format(i + 1))
            graph = nx.gnm_random_graph(nodes, edges, seed=None, directed=False)
            nx.draw(graph, with_labels=True)
            plt.savefig("outputs/n_{}_e_{}_pq_{}_run_{}.png".format(nodes, edges, priorityQueueType, i))
            plt.figure().clear()
            dijkstra = Dijkstra.Dijkstra()
            dijkstra.run(graph, PriorityQueue)
