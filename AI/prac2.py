def bfs(graph,start):
    visited=[]
    queue=[]
    visited.append(start)
    queue.append(start)
    print("BFS:")
    while queue:
        node=queue.pop(0)
        print(node,end=" ")
        for n in graph[node]:
                   if n not in visited:
                       visited.append(n)
                       queue.append(n)
            
            
 

    
   


def shortest_path(graph,start,end):
    queue=[[start]]
    visited=[]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node==end:
            return path
        if node not in visited:
            for n in graph[node]:
                new_path=path+[n]
                queue.append(new_path)
            visited.append(node)
    return None

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E': [], 
    'F': []
}
bfs(graph,'A')
print('\nShortest Path',shortest_path(graph,'A','F'))





