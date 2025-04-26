import heapq

class Edge:
    def __init__(self, target, weight):
        # Initialize an edge with target vertex and weight
        self.target = target
        self.weight = weight


class Graph:
    def __init__(self, vertices):
        # Initialize a graph with a given number of vertices
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, source, target, weight):
        # Add a directed edge from source to target with given weight
        self.adjacency_list[source].append(Edge(target, weight))

    def dijkstra(self, start_vertex):
        # Initialize distances array with infinity
        distances = [float('inf')] * self.vertices
        distances[start_vertex] = 0

        # Priority queue to select the vertex with the smallest distance
        pq = []
        heapq.heappush(pq, (0, start_vertex))

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # Skip if we have already found a better path
            if current_distance > distances[current_vertex]:
                continue

            # Explore neighbors
            for edge in self.adjacency_list[current_vertex]:
                neighbor = edge.target
                new_dist = current_distance + edge.weight

                # Update distance if a shorter path is found
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        # Print the shortest distances from the source
        print(f"Shortest distances from source vertex {start_vertex}:")
        for i in range(self.vertices):
            print(f"Vertex {i}: {distances[i]}")


def main():
    # Create a graph with 5 vertices
    graph = Graph(5)

    # Add edges to the graph
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 1, 3)
    graph.add_edge(2, 3, 9)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 0, 7)
    graph.add_edge(4, 3, 4)

    # Run Dijkstra's algorithm from source vertex 0
    graph.dijkstra(0)


if __name__ == "__main__":
    main()

