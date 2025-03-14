
def inorder_traverse(current, graph, visited):
    if not current or visited[current]:
        return

    visited[current] = True
    neighbors = graph.get(current, [])

    if neighbors:
        inorder_traverse(neighbors[0], graph, visited)

    print(current, end=" ")

    for next_node in neighbors[1:]:
        inorder_traverse(next_node, graph, visited)


G = {
    1: [2, 3],
    2: [5, 6],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}
max_node = max(G.keys())
matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]
for node in G:
    for neighbor in G[node]:
        matrix[node][neighbor] = 1

print("Adjacency Matrix:")
for i in range(1, max_node + 1):
    print(" ".join(map(str, matrix[i][1:])))

start_node = int(input("\nEnter node: "))
visited = [False] * (max(G.keys()) + 1)

if not start_node or visited[start_node]:
    print("Invalid start node or node already visited.")
    exit()

visited[start_node] = True
neighbors = G.get(start_node, [])

if neighbors:
    inorder_traverse(neighbors[0], G, visited)

print(start_node, end=" ")

for next_node in neighbors[1:]:
    inorder_traverse(next_node, G, visited)


