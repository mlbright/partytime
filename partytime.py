#!/usr/bin/python

import sys
from collections import defaultdict
from random import randint

def _next_int():
    return int(sys.stdin.readline())

class PartyTime(object):
    
    def __init__(self,G,costs,F):
        self.costs = costs
        self.max_ = sum(costs)
        self.G = G
        self.F = F
        self.best = set(G.keys())

    def solve(self):
        source = randint(0,self.F-1)
        self._search(source)

    def _all_friends(self,visited):
        for friend in range(self.F):
            if friend not in visited:
                return False
        return True
    
    def _search(self,curr,cost=0,visited=set(),used=set()):
        if cost >= self.max_:
            return
        if self._all_friends(visited) and cost < self.max_: # and len(visited) < len(self.best):
            print "best"
            self.max_ = cost
            self.best = set(used)
            print self.max_
            print self.best
            return
        for next in self.G[curr]:
            if next not in visited:
                visited.add(next)
                self._search(next,cost+self.costs[next],visited,used|set([next]))

    def output(self):
        print self.best
        print "%d %d" % (self.max_,len(self.best))


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
