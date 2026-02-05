def dfs(graph,node,visited):
    print("Visiting:",node)
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)


graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E': [], 
    'F': []
}

visited=set()
dfs(graph,'A',visited)