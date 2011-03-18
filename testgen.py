import sys
import optparse
import random
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    T = 1
    F = random.randint(1,11)
    N = random.randint(F+1,250)
    M = random.randint(N-1,N*(N-1)/2)
    G = nx.generators.random_graphs.gnm_random_graph(N,M)
    print "F=%d N=%d M=%d" % (F,N,M)
    nx.draw(G)
    plt.savefig("ex.png")
