import sys
from optparse import OptionParser

from source import FibHeap
from source import MinHeap
from source import Dijkstra

USAGE = """
USAGE : python3 main.py <options>
Example : python3 main.py -p min-heap -n 1000 -d 1.6 -r 5
            runs dijkstra 5 times using min-heap priority queue 
            on a graph with 1000 nodes and approximate density 1.6
"""


def default(default_):
    return default_ + ' [Default: %default]'


def fillOption(option, strLead):
    return option + " --" + "-" * (len(strLead) - len(option)) + " "


def printOptions(options):
    print("============ Options ============")
    strLead = "Priority Queue"
    print(fillOption("Priority Queue", strLead), options.priorityqueue)
    print(fillOption("Nodes", strLead), options.nodes)
    print(fillOption("Density", strLead), options.density)
    print(fillOption("Runs", strLead), options.runs)


def parseInput(argv):
    parser = OptionParser(USAGE)

    parser.add_option('-p', '--priorityqueue', help=default('The type of priority queue'),
                      choices=['min-heap', 'fib-heap'], default='min-heap')
    parser.add_option('-n', '--nodes', help=default('Nodes'), default=20)
    parser.add_option('-d', '--density', help=default('Approximate density'), default=1.5)
    parser.add_option('-r', '--runs', help=default('Runs'), default=1)

    options, junk = parser.parse_args(argv)
    if len(junk) != 0:
        raise Exception('Command line input not understood: ' + str(junk))

    printOptions(options)

    pqClass = MinHeap.MinHeap if options.priorityqueue == "min-heap" else FibHeap.FibHeap
    return (pqClass, options.nodes, options.density, int(options.runs))


if __name__ == '__main__':
    PriorityQueue, nodes, density, runs = parseInput(sys.argv[1:])
    for i in range(0, runs):
        print("============ Run {} ============".format(i))
        dijkstra = Dijkstra.Dijkstra()
