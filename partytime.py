#!/usr/bin/python

import sys
from collections import defaultdict
from random import randint
import time

def _next_int():
    return int(sys.stdin.readline())

class PartyTime(object):
    
    def __init__(self,G,costs,F):
        self.costs = costs
        self.G = G
        self.F = F

    def solve(self):
        self.start = randint(0,self.F - 1)
        print "%d" % (self.start)
        self.cost = sum(self.costs)
        print "%d" % (self.cost)
        self.best = set(self.G.keys())
        print self.best
        friends = set(range(self.F))
        self._search(self.G,self.start,friends)

    def _collapse(self,graph,path):

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
    
        return G


    def _search(self,graph,curr,friends,cost=0,used=set(),path=set()):
        if cost > self.cost or (cost == self.cost and len(used) >= len(self.best)):
            return
        elif (curr in friends) and path:
            if curr != self.start:
                friends = friends - set([curr])
            if len(friends) == 1:
                if cost <= self.cost:
                    self.cost = cost
                    self.best = set(used)
                    print self.cost
                    print self.best
                return
            self._search(self._collapse(graph,path),self.start,friends,cost,used)
        else:
            for next in graph[curr]:
                if next not in path:
                    self._search(graph,next,friends,cost+self.costs[next],used|set([next]),path|set([next]))


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
