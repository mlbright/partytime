#!/usr/bin/python

import sys
from collections import defaultdict
from random import randint

def _next_int():
    return int(sys.stdin.readline())

class PartyTime(object):
    
    def __init__(self,G,costs,F):
        self.costs = costs
        self.G = G
        self.F = F

    def solve(self):
        self.best_friend = randint(0,self.F-1)
        self.max_ = sum(self.costs)
        self.best = set(self.G.keys())
        print self.max_
        print self.best
        self._search(self.G,self.best_friend)

    def _all_friends(self,curr,used):
        for friend in range(self.F):
            if friend not in used:
                return False
        return True

    def _is_friend(self,curr):
        if curr < self.F:
            return True
        else:
            return False

    def _collapse(self,graph,path):

        sink  = self.best_friend
        G = defaultdict(set)

        for s in graph:
            for d in graph[s]:
                if d not in path and s not in path:
                    G[s].add(d)
                elif s not in path and d in path:
                    G[s].add(sink)
                elif s in path and d not in path:
                    G[sink].add(d)
    
        return G



    def _search(self,graph,curr,cost=0,used=set(),path=set()):
        if cost > self.max_:
            return
        if cost == self.max_ and len(used) >= len(self.best):
            return
        print used
        if self._is_friend(curr) and path:
            G = self._collapse(graph,path)
            if self._all_friends(curr,used):
                if cost <= self.max_:
                    self.max_ = cost
                    self.best = set(used)
                return
            self._search(G,self.best_friend,cost,used)
        else:
            for next in self.G[curr]:
                if next not in path or next < self.F:
                    self._search(graph,next,cost+self.costs[next],used|set([next]),path|set([next]))

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
