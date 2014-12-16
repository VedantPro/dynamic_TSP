import matplotlib.pyplot as plt
from random import randint
import itertools
import math
import time

#Global Variables
points = []
Y = []
time_tot = float
def val(x):
        y = [randint(1,10),randint(0,x)]
        return y

#for calculating distance between 2 points
def length(x,y):
        #return math.sqrt( ((val(x))[0]-(val(y))[0])**2 +  ((val(x))[1]-(val(y))[1])**2 )
        return math.sqrt( (Y[x][0]-Y[y][0])**2 + (Y[x][1]-Y[y][1])**2)

def TSP_dynamic(points):
        global time_tot
        #calc all lengths
        dist = [[length(x,y) for y in points] for x in points]
        #initial value - just distance from 0 to every other point + keep the track of edges
        A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate( dist[0][1:])}
        size = len(points)

        tt = time.time()

        for m in range(2, size):
                B = {}
                for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, size), m)]:
                        #recursively moving up i.e. adding more and more edges
                        for j in S - {0}:
                                #finding the minimum among all the possible paths
                                B[(S, j)] = min( [(A[(S-{j},k)][0] + dist[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])
                A = B
        #adding final to initial path
        res = min([(A[d][0] + dist[0][d[1]], A[d][1]) for d in iter(A)])

        time_tot = float(time.time()) - float(tt)
        return res

def Prims(points):

        pass

def main():
        global points,Y
        n = int(raw_input("Type the no. of vertices:" ))
        points = list(range(0,n))
        for a in points:
                Y.append(val(a))
        print "Random points are:\n" + str(Y)
        result = TSP_dynamic(points)
        result[1].append(0)
        
        print "\nTotal distance travelled:       " + str(result[0])
        print "\nTravelling root is:             " + str(result[1])

        plt.axis()
        ptsX = [Y[i][0] for i in result[1] ]
        ptsY = [Y[i][1] for i in result[1] ]
        
        print "Total time taken: " + str(float(time_tot))
        plt.plot(ptsX,ptsY,'bo-')
        plt.show()
        

if __name__ == "__main__":
        main()
