class G:
    def __init__(self,V):
        self.V=V
        self.graph=[[0 for g in range(V)] for b in range(V)]
    def printGraph(self,V,key,pt):
        for g in range(1,V):
            print(str(pt[g]),"-",str(g),":",str(key[g]))
    def prim(self,src):
        V=self.V
        maxint=9999
        visited=[False for g in range(V)]
        key=[maxint for g in range(V)]
        pt=[None for g in range(V)]
        key[src]=0
        pt[src]=-1
        for count in range(V):
            u=findMin(key,V,visited)
            visited[u]=True
            for v in range(V):
                if(self.graph[u][v]>0 and visited[v]==False and self.graph[u][v]<key[v]):
                    key[v]=self.graph[u][v]
                    pt[v]=u
        self.printGraph(V,key,pt)
def findMin(key,v,visited):
    minint=99999
    minindex=-1
    for g in range(v):
        if(key[g]<minint and visited[g]==False):
            minint=key[g]
            minindex=g
    return minindex
g=G(5)
g.graph=[[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
g.prim(0)

# Output:
# 0 - 1 : 2
# 1 - 2 : 3
# 0 - 3 : 6
# 1 - 4 : 5