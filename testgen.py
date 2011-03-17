import sys
import optparse
import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_test():
    pass

if __name__ == "__main__":
    T = 1
    N = 100
    F = 11
    M = 1000
    G = nx.generators.random_graphs.random_regular_graph(5,100)
    nx.draw(G)
    plt.savefig("ex.png")
    components = nx.connected_components(G)
    print components
