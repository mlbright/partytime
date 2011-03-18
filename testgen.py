import sys
from random import randint
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == "__main__":
    T = 1
    F = randint(1,11)
    N = randint(F+1,250)
    M = randint(N-1,N*(N-1)/2)
    G = nx.generators.random_graphs.gnm_random_graph(N,M)
    #for i in xrange(0,G.number_of_nodes()):
    #    G.node[i]['cost'] = randint(0,1000)
    #print "F=%d N=%d M=%d" % (F,N,M)
    nx.draw(G)
    plt.savefig("ex.png")
    if nx.algorithms.components.connected.is_connected(G):
        #print "yay, graph is connected"
        pass
    else:
        #print "no no no, graph is not connected"
        sys.exit(0)

    """
    source = randint(0,F)    
    plt.cla()
    tree   = nx.algorithms.traversal.depth_first_search.dfs_tree(G,source)
    nx.draw(tree)
    plt.savefig("dfs_tree.png")

    for node in nx.algorithms.traversal.depth_first_search.dfs_successors(G,source):
        print node

    S = partytime(G,source)
    """

    print T
    print N
    print F
    print M
    for (u,v) in G.edges_iter():
        print "%d %d" % (u,v)
    for _ in xrange(0,G.number_of_nodes()):
        print "%d" % (randint(0,1000))
