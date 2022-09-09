infinity = float("inf")

def make_graph():
    # identical graph from the YouTube video: https://youtu.be/obWXjtg0L64
    # tuple = (cost, to_node)
    return {
        'S': [(8, 'E'), (10, 'A')],
        'A': [(2, 'C')],
        'B': [(1, 'A')],
        'C': [(-2, 'B')],
        'D': [(-4, 'A'), (-1, 'C')],
        'E': [(1, 'D')],
    }


# input graph is assumed to have no negative cycles
def bellman_ford(G, start):
    shortest_paths = {}
    
    for node in G:
        shortest_paths[node] = infinity

    shortest_paths[start] = 0
    size = len(G)

    for _ in range(size - 1):
        for node in G:
            for edge in G[node]:
                cost = edge[0]
                to_node = edge[1]
                if shortest_paths[node] + cost < shortest_paths[to_node]:
                    shortest_paths[to_node] = shortest_paths[node] + cost

    return shortest_paths


def main():
    G = make_graph()
    start = 'S'

    shortest_paths = bellman_ford(G, start)
    print(f'Shortest path from {start}: {shortest_paths}')

main()
