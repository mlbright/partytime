import sys
from random import randint, shuffle
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == "__main__":
    T = 1
    F = randint(1,11)
    N = randint(F+1,250)
    M = randint(N-1,N*(N-1)/2)
    G = nx.generators.random_graphs.gnm_random_graph(N,M)
    nx.draw(G)
    plt.savefig("ex.png")

    print T
    print N
    print F
    print M
    
    remapping = range(N)
    shuffle(remapping)
    for (u,v) in G.edges_iter():
        print "%d %d" % (remapping[u],remapping[v])
    for _ in xrange(G.number_of_nodes()):
        print "%d" % (randint(0,1000))
