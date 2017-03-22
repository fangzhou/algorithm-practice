import unittest

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def topSort(graph):
    """
    BFS based topological sort
    """
    results = []
    indegree = {}
    _indget = indegree.get

    # Build a map for each node's indegree
    for node in graph:
        for neighbor in node.neighbors:
            indegree[neighbor] = _indget(neighbor, 0) + 1

    bfsq = []
    # Starting BFS from node without indegree
    for node in graph:
        if node not in indegree:
            bfsq.append(node)
            results.append(node)

    while len(bfsq) > 0:
        curr = bfsq.pop(0)
        for neighbor in curr.neighbors:
            # Decrease indegree for visited edges
            indegree[neighbor] = indegree[neighbor] - 1
            if indegree[neighbor] == 0:
                results.append(neighbor)
                bfsq.append(neighbor)

    return results

def build_graph_from_input(inputstr):
    """
    Build the graph data structure from string input.
    String input format:
      1. '#' character used to separate different nodes
      2. ',' character used inside a node ('#' separated substring), first
         character would be current node's label, and following characters
         are the neighbouring nodes' labels.
    """
    labelsmap = dict()
    node_list = [c.split(',') for c in inputstr.split('#')]
    graph_list = []

    for n in node_list:
        _label = n[0]
        if _label not in labelsmap:
            labelsmap[_label] = DirectedGraphNode(_label)

        for neighbor_idx in xrange(1, len(n)):
            _nlabel = n[neighbor_idx]
            if _nlabel not in labelsmap:
                labelsmap[_nlabel] = DirectedGraphNode(_nlabel)
                labelsmap[_label].neighbors.append(labelsmap[_nlabel])
            else:
                labelsmap[_label].neighbors.append(labelsmap[_nlabel])

    for label, node in labelsmap.iteritems():
        # print label, node, [n.label for n in node.neighbors]
        graph_list.append(node)

    return graph_list

class testTopoSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_0_graph_build(self):
        inputstr = "0,1,2,3,4#1,3,4#2,1,4#3,4#4"
        graph = build_graph_from_input(inputstr)
        print graph

    def test_1(self):
        inputstr = "0,1,2,3,4#1,3,4#2,1,4#3,4#4"
        graph = build_graph_from_input(inputstr)
        R = topSort(graph)
        print [n.label for n in R]

    def test_2(self):
        inputstr = "0,3,6,7#1,8,9,3,5,0#2,0,9,3,6,8#3,6,7#4,0,1,6,7,8,9#5,0,8,2,3#6#7,6#8,0,3,6,7#9,8,6,7"
        graph = build_graph_from_input(inputstr)
        R = topSort(graph)
        print [n.label for n in R]

if __name__ == "__main__":
    unittest.main()
