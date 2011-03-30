#!/usr/bin/python

import sys
from collections import defaultdict
from random import randint

def _next_int():
    return int(sys.stdin.readline())

if __name__ == "__main__":

    T = _next_int()
    for _ in range(T):
        N = _next_int()
        F = _next_int()
        M = _next_int()

        #print "%d %d %d" % (N,F,M)    
        G = defaultdict(set)
        for _ in xrange(M):
            u,v = sys.stdin.readline().strip().split()
            u,v = int(u),int(v)
            #print "%d %d" % (u,v)
            G[u].add(v)
            G[v].add(u)
            
        #print G

        costs = []
        for _ in xrange(N):
            costs.append(int(_next_int()))

        p  = PartyTime(G,costs,F)
        p.solve()
        p.output()
