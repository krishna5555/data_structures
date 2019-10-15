class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addNode(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        visited=[False]*len(self.graph)
        q=[]
        q.append(s)
        visited[s]=True
        while(len(q)!=0):
            t=q.pop(0)
            print(t,end=" ")
            for x in self.graph[t]:
                if(x<=len(self.graph[t]) and visited[x]==False):
                    q.append(x)
                    visited[x]=True
                elif(x>len(self.graph[t])):
                    q.append(x)
g=Graph()
g.addNode(0,1)
g.addNode(0,2)
g.addNode(1,3)
g.addNode(2,4)
g.bfs(0)
#bfs traversal-0,1,2,3,4