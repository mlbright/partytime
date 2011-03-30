#!/usr/bin/python

import sys
import time

def _next_int():
    return int(sys.stdin.readline())

class PartyTime(object):

    def __init__(self):
        self.final = sys.maxint
    
    def run(self):
        N = self.N
        F = self.F
        d = [ [ sys.maxint for i in range(N) ] for j in range(N) ]
        for i in range(N):
            for j in range(N):
                if i != j:
                    if self.friends[i][j]:
                        d[i][j] = self.food[j]

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        best = [[sys.maxint] * N]
        for set in xrange(1, 1 << F):
            best.append([sys.maxint] * N)
            if (set & (set - 1)) == 0:
                first = 0
                while (set & (1 << first)) == 0:
                    first += 1
                best[set][first] = self.food[first]
            else:
                subset = (set - 1) & set
                while subset > 0:
                    for i in range(N):
                        best[set][i] = min(best[set][i], best[subset][i] + best[subset ^ set][i] - self.food[i])
                    subset = (subset - 1) & set

            for i in range(N):
                for j in range(N):
                    best[set][j] = min(best[set][j], best[set][i] + d[i][j])

        for i in range(N):
            self.final = min(self.final, best[(1 << F) - 1][i])

    def output(self):
        print "%d %d" % (self.final / 1000, self.final % 1000)

    def input(self):
        T = _next_int() # test with T == 1 for now

        N = _next_int()
        F = _next_int()
        M = _next_int()

        friends = [ [ False for i in range(N) ] for j in range(N) ]
        for _ in xrange(M):
            u,v = sys.stdin.readline().strip().split()
            u,v = int(u),int(v)
            friends[u][v] = True
            friends[v][u] = True
            
        food = []
        for _ in xrange(N):
            food.append(_next_int() * 1000 + 1);

        self.N = N
        self.F = F
        self.food = food
        self.friends = friends


if __name__ == "__main__":

    #t1 = time.time()
    solver = PartyTime()
    solver.input()
    solver.run()
    solver.output()
    #t2 = time.time()
    #print "%.2f" % (t2 - t1)
