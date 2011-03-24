#!/usr/bin/python

import sys
from collections import defaultdict
from random import randint

def _next_int():
    return int(sys.stdin.readline())

class PartyTime(object):
    
    def __init__(self,G,costs,F):
        self.G = G
        self.food = costs
        self.F = F

    def _collapse(self,graph,sol,path):

        sink  = self.start
        G = defaultdict(set)

        for s in graph:
            for d in graph[s]:
                if s not in path and d not in path:
                    G[s].add(d)
                elif s not in path and d in path:
                    G[s].add(sink)
                elif s in path and d not in path:
                    G[sink].add(d)
    
        return G, sol | path

    def solve(self):
        self.friends = set(range(self.F))
        self.start = self.friends.pop()
        self.friends.add(self.start)
        self.cost = sum(self.food)
        self.best = set(self.G.keys())
        self._search(self.G,self.start)

    def _search(self,graph,curr,cost=0,sol=set(),path=set()):
        if cost >= self.cost:
            return
        if curr in self.friends and path:
            print "here"
            if self.friends.issubset(sol):
                if cost <= self.cost:
                    self.cost = cost
                    self.best = set(sol)
                return
            _graph,_sol = self._collapse(graph,sol,path)
            self._search(_graph,self.start,cost,_sol)
        else:
            for next in graph[curr]:
                if next not in path:
                    self._search(graph,next,cost+self.food[curr],sol,path|set([curr]))


    def output(self):
        print self.best
        print "%d %d" % (self.cost,len(self.best))


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
