#!/usr/bin/python

import sys
from collections import defaultdict
from random import randint

def _next_int():
    return int(sys.stdin.readline())

class PartyTime(object):
    
    def __init__(self,G,costs,F):
        self.costs = costs
        self.total = sum(costs)
        self.G = G
        self.F = F
        self.friends = set(range(F))
        self.best = set(G.keys())

    def solve(self):
        source = randint(0,self.F-1)
        self.search(source,self.total,set(),self.friends.copy())

    def search(self,curr,cost,visited,friends):
        if cost > self.total:
            return
        if curr in friends:
            friends.remove(curr)
            if len(friends) == 0:
                self.total = cost
                self.best = set(visited)
                return
        for next in self.G[curr]:
            if next not in visited:
                self.search(next,cost+self.costs[next],visited | set([next]),friends | set())

    def output(self):
        print "%d %d" % (self.total,len(self.best))


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
