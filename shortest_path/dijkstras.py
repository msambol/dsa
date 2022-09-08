def make_graph():
    # same graph in YouTube video: https://youtu.be/_lHSawdgXpI
    # tuple = (cost, to_node)
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    }


def dijkstras(G, start='A'):
    shortest_paths = {}
    unvisited = list(G.keys())
    infinity = float("inf")

    for node in unvisited:
        shortest_paths[node] = infinity

    shortest_paths[start] = 0

    while unvisited:
        min_node = None

        for node in unvisited:
            if min_node is None:
                min_node = node
            elif shortest_paths[node] < shortest_paths[min_node]:
                min_node = node

        for edge in G[min_node]:
            cost = edge[0]
            to_node = edge[1]

            if cost + shortest_paths[min_node] < shortest_paths[to_node]:
                shortest_paths[to_node] = cost + shortest_paths[min_node]

        unvisited.remove(min_node)

    return shortest_paths


def main():
    G = make_graph()
    start = 'A'
    shortest_paths = dijkstras(G, start)

    print(f'Shortest path from {start}: {shortest_paths}')

main()
