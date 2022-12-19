import time

from source.dijkstraHandler import DijkstraHandler
from source.fibHeap import FibHeap
from source.minHeap import MinHeap

if __name__ == '__main__':
    densities = [d / 10 for d in range(2, 10)]
    nodes = [100 * i for i in range(1, 11)]
    print("Densities : ", densities)
    print("Nodes : ", nodes)
    minheap_runtimes = {}
    fibheap_runtimes = {}
    for density_ in densities:
        print("d={}".format(density_))
        minheap_runtimes[density_] = {}
        fibheap_runtimes[density_] = {}
        for node_ in nodes:
            print("n={}".format(node_))
            edges_ = int(density_ * node_ * (node_ - 1) / 2)

            t_minheap = time.process_time_ns()
            DijkstraHandler.run(node_, edges_, 5, MinHeap, None, mute=True)
            t_minheap = (time.process_time_ns() - t_minheap) * 1e-6
            minheap_runtimes[density_][node_] = t_minheap
            print("minheap runtime {}".format(t_minheap))

            t_fibheap = time.process_time_ns()
            DijkstraHandler.run(node_, edges_, 5, FibHeap, None, mute=True)
            t_fibheap = (time.process_time_ns() - t_fibheap) * 1e-6
            fibheap_runtimes[density_][node_] = t_fibheap
            print("fibheap runtime {}".format(t_fibheap))

            print("--------")
        print("========")
    print("================")
    print("MinHeap : ", minheap_runtimes)
    print("FibHeap : ", fibheap_runtimes)
