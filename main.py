import sys
from optparse import OptionParser

from source.dijkstraHandler import DijkstraHandler
from source.fibHeap import FibHeap
from source.minHeap import MinHeap

USAGE = """
USAGE : python3 main.py <options>
Example : python3 main.py -p min-heap -n 20 -d 0.6 -r 6
            runs dijkstra 6 times using min-heap priority queue 
            on a graph with 20 nodes and density 0.6
"""


def default(default_):
    return default_ + ' [Default: %default]'


def fillOption(option, strLead):
    return option + " --" + "-" * (len(strLead) - len(option)) + " "


def parseInput(argv):
    parser = OptionParser(USAGE)

    parser.add_option('-p', '--priorityqueue', help=default('The type of priority queue'),
                      choices=['min-heap', 'fib-heap', 'def'], default='def')
    parser.add_option('-n', '--nodes', help=default('Nodes'), default=20)
    parser.add_option('-d', '--density', help=default('Approximate density: between 0 and 1'), default=0.2)
    parser.add_option('-r', '--runs', help=default('Runs'), default=1)

    options, junk = parser.parse_args(argv)
    if len(junk) != 0:
        raise Exception('Command line input not understood: ' + str(junk))

    pqClass = MinHeap if options.priorityqueue == "min-heap" else FibHeap
    pqClass = None if options.priorityqueue == "def" else pqClass
    nodes_ = int(options.nodes)
    density_ = float(options.density)
    runs_ = int(options.runs)
    edges_ = int(density_ * nodes_ * (nodes_ - 1) / 2)

    print("============ Options ============")
    strLead = "Priority Queue"
    print(fillOption("Priority Queue", strLead), options.priorityqueue)
    print(fillOption("Nodes", strLead), str(nodes_))
    print(fillOption("Edges", strLead), str(edges_))
    print(fillOption("Density", strLead), str(density_))
    print(fillOption("Runs", strLead), str(runs_))

    return (pqClass, nodes_, edges_, density_, runs_, options.priorityqueue)


"""
Demo run:
python3 main.py -p def -n 20 -d 0.3 -r 3
python3 main.py -p fib-heap -n 50 -d 0.4 -r 1
python3 main.py -p min-heap -n 10 -d 0.6 -r 2
"""
if __name__ == '__main__':
    PriorityQueue, nodes, edges, density, runs, priorityQueueType = parseInput(sys.argv[1:])
    DijkstraHandler.run(nodes, edges, runs, PriorityQueue, priorityQueueType)
