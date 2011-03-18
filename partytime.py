#!/usr/bin/python

import sys

def _next_int():
    return int(sys.stdin.readline())

if __name__ == "__main__":

    T = _next_int()
    for _ in range(T):
        N = _next_int()
        F = _next_int()
        M = _next_int()

        #print "%d %d %d" % (N,F,M)    
        for _ in xrange(M):
            u,v = sys.stdin.readline().strip().split()
            u,v = int(u),int(v)
            print "%d %d" % (u,v)

        costs = []
        for _ in xrange(N):
            costs.append(int(sys.stdin.readline()))

        print costs
