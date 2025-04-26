class Edge:
    def __init__(self, source, destination, weight):
        # Initialize an edge with source, destination and weight
        self.source = source
        self.destination = destination
        self.weight = weight


def bellman_ford(vertices, edges_count, edges, source):
    # Initialize distance to all vertices as infinite and predecessor as -1
    distance = [float('inf')] * vertices
    predecessor = [-1] * vertices
    distance[source] = 0

    # Relax edges repeatedly (vertices - 1 times)
    for i in range(1, vertices):
        for j in range(edges_count):
            u = edges[j].source
            v = edges[j].destination
            weight = edges[j].weight

            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u

    # Check for negative-weight cycles
    for j in range(edges_count):
        u = edges[j].source
        v = edges[j].destination
        weight = edges[j].weight

        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Graph contains a negative-weight cycle")
            return

    print_solution(distance, predecessor, source)


def print_solution(distance, predecessor, source):
    # Print the shortest distance and path from source to each vertex
    print("Vertex Distance from Source and Path:")
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            print(f"Vertex {i}: No path from source")
        else:
            print(f"Vertex {i} : {distance[i]} (Path: ", end='')
            print_path(i, predecessor)
            print(")")


def print_path(current, predecessor):
    # Recursively print the path from source to current vertex
    if current == -1:
        return
    print_path(predecessor[current], predecessor)
    print(f"{current} ", end='')


def main():
    # Define number of vertices and edges
    vertices = 5
    edges_count = 10

    # Create the edges of the graph
    edges = [None] * edges_count

    edges[0] = Edge(0, 1, 6)
    edges[1] = Edge(0, 2, 7)
    edges[2] = Edge(1, 3, 5)
    edges[3] = Edge(1, 2, 8)
    edges[4] = Edge(1, 4, -4)
    edges[5] = Edge(2, 3, -3)
    edges[6] = Edge(2, 4, 9)
    edges[7] = Edge(3, 1, -2)
    edges[8] = Edge(4, 0, 2)
    edges[9] = Edge(4, 3, 7)

    # Run Bellman-Ford algorithm from source vertex 0
    bellman_ford(vertices, edges_count, edges, 0)


if __name__ == "__main__":
    main()

