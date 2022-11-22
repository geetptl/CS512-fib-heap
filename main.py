import sys
from optparse import OptionParser

from source import FibHeap
from source import MinHeap
from source import Dijkstra

USAGE = """
USAGE : python3 main.py <options>
Example : python3 main.py -pq min-heap -n 1000 -d 1.6
            runs dijkstra using min-heap priority queue 
            on a graph with 1000 nodes and approximate density 1.6
"""


def default(default_):
    return default_ + ' [Default: %default]'


def parseInput(argv):
    parser = OptionParser(USAGE)

    parser.add_option('-p', '--priorityqueue', help=default('The type of priority queue'),
                      choices=['min-heap', 'fib-heap'], default='min-heap')
    parser.add_option('-n', '--nodes', help=default('Nodes'), default=20)
    parser.add_option('-d', '--density', help=default('Approximate density'), default=1.5)

    options, junk = parser.parse_args(argv)
    if len(junk) != 0:
        raise Exception('Command line input not understood: ' + str(junk))

    print("======Starting======")
    print("Priority Queue : \t\t", options.priorityqueue)
    print("Nodes : \t\t", options.nodes)
    print("Density : \t\t", options.density)

    pqClass = MinHeap.MinHeap if options.priorityqueue == "min-heap" else FibHeap.FibHeap
    return (pqClass, options.nodes, options.density)


if __name__ == '__main__':
    PriorityQueue, nodes, density = parseInput(sys.argv[1:])
    dijkstra = Dijkstra.Dijkstra()
    dijkstra.run(None, "source", PriorityQueue)
