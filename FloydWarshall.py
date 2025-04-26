INF = 99999  # Representing infinity (no direct path)

def floyd_warshall(graph, vertices):
    # Initialize distance matrix with input graph values
    dist = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Copy the input graph to distance matrix
    for i in range(vertices):
        for j in range(vertices):
            dist[i][j] = graph[i][j]

    # Applying Floyd-Warshall Algorithm
    for k in range(vertices):
        # Pick all vertices one by one as intermediate vertices
        for i in range(vertices):
            for j in range(vertices):
                # Update dist[i][j] if a shorter path is found through vertex k
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Print the final shortest distance matrix
    print_solution(dist, vertices)

def print_solution(dist, vertices):
    print("Shortest distances between every pair of vertices:")
    for i in range(vertices):
        for j in range(vertices):
            if dist[i][j] == INF:
                print("INF", end=" ")  # No path between i and j
            else:
                print(f"{dist[i][j]}", end="   ")  # Print shortest distance
        print()

def main():
    vertices = 4  # Number of vertices in the graph

    # Representation of the graph as an adjacency matrix
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]

    # Run the Floyd-Warshall algorithm
    floyd_warshall(graph, vertices)

if __name__ == "__main__":
    main()

