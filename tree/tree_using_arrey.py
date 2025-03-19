#arrey of edges:direated graph([start,end])
n=8

A=[[0,3],[0,1],[3,7],[3,6],[3,4],[1,2],[4,2],[4,5],[5,2]]

#convering arrey of edges to an adjeceny matrix
print("---------------------convert to adjecency matrix----------------------")

M=[]
for i in range(n):
    M.append([0]*n)
for u,v in A:
    M[u][v]=1
    
for i in range(n):#just to see the ouput 
    print(M[i])
    
print("------------------converting to adjecency list-------------------------")
    
from collections import defaultdict

d=defaultdict(list)
for x,y in A:
    d[x].append(y)

for x,y in d.items():#print all
    print(x,"-->",y)
    
print("--------------------accesing the element we want from both the matrix one and the line one--------")

print(M[0])
print(d[0])

print("-------------dfs with recurrison:O(v+n)-----------------------------")

source=0
seen=set()
seen.add(source)

def dfs_recurr(node):
    print(node)
    
    for neigh in d[node]:
        if neigh not in seen:
            seen.add(neigh)
            dfs_recurr(neigh)
    

dfs_recurr(source)

print("-------------dfs with iteration:O(v+n)-----------------------------")

source=0
seen=set()
seen.add(source)
stack=[source]

while stack:
    curr=stack.pop()
    print(curr)
    
    for naghi in d[curr]:
        if naghi not in seen:
            seen.add(naghi)
            stack.append(naghi)
            
print("-----------------bfs using queue--------------------------")
from collections import deque

source=0
seen=set()
seen.add(source)

q=deque()
q.append(source)

while q:
    
    curr=q.popleft()
    
    print(curr)
    for neghi in d[curr]:
        if neghi not in seen:
            seen.add(neghi)
            q.append(neghi)




