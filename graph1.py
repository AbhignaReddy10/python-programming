num_vertices=4
adj_matrix = [[0]*num_vertices for _ in range(num_vertices)]
edges= [(0,1),(0,2),(1,2),(1,3),(2,3)]
for u,v in edges:
    adj_matrix[u][v]= 1
    adj_matrix[v][u]=1

print("adjacency matrix reprentation of the graph")
for row in adj_matrix:
    print(row)
