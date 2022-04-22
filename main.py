from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
      tofrontier = set()
      toresult = set()
      toremove = set()
      for node in frontier:
        toremove.add(node)
        neighbors = set(graph[node])
        for neighbor in neighbors:
          toresult.add(neighbor)
        for node in toresult:
          if node not in result:
            result.add(node)
            tofrontier.add(node)
      for node in toremove:
        frontier.remove(node)
      for node in tofrontier:
        frontier.add(node)
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']




def connected(graph):
  nodes = graph.keys()
  i = 0
  startnode = ''
  while i < 1:
    for node in nodes:
      startnode = node
      i += 1
  return nodes == reachable(graph, startnode)

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
  if connected(graph) == True:
    return 1
  else:
    components = 0
    nodes = set(graph.keys())
    nodestocheck = nodes
    while len(nodestocheck) > 0:
      components += 1
      i=0
      while i < 1:
        for node in nodestocheck:
          startnode = node
          i += 1
      reachables = reachable(graph, startnode)
      for node in reachables:
        nodestocheck.remove(node)
    return components
  """
    Returns:
      the number of connected components in an undirected graph
  """
  

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2
