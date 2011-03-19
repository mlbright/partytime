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
        friends = set(range(self.F))
        self._search(self.G,self.best_friend,friends)

    def _all_friends(self,friends,used):
        for friend in friends:
            if friend not in used:
                return False
        return True

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



    def _search(self,graph,curr,friends,cost=0,used=set(),path=set()):
        print friends
        if cost > self.max_:
            return
        if cost == self.max_ and len(used) >= len(self.best):
            return
        if curr in friends and path:
            G = self._collapse(graph,path)
            if self._all_friends(friends-set([curr]),used):
                if cost <= self.max_:
                    self.max_ = cost
                    self.best = set(used)
                return
            else:
                self._search(G,self.best_friend,friends - set([curr]),cost,used)
        else:
            for next in self.G[curr]:
                if next not in path or next < self.F:
                    self._search(graph,next,friends,cost+self.costs[next],used|set([next]),path|set([next]))

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
