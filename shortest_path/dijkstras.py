import heapq


infinity = float("inf")


def make_graph():
    # identical graph as the YouTube video: https://youtu.be/_lHSawdgXpI
    # tuple = (cost, to_node)
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    }


def dijkstras_heap(G, start='A'):
    shortest_paths = {} 
    visited = set()
    heap = []

    for node in G.keys():
        shortest_paths[node] = infinity

    shortest_paths[start] = 0 
    visited.add(start)

    heapq.heappush(heap, (0, start))

    while heap:
        (distance, node) = heapq.heappop(heap)
        visited.add(node)

        for edge in G[node]:
            cost, to_node = edge

            if (to_node not in visited) and (distance + cost < shortest_paths[to_node]):
                shortest_paths[to_node] = distance + cost
                heapq.heappush(heap, (shortest_paths[to_node], to_node))

    return shortest_paths


def dijkstras(G, start='A'):
    shortest_paths = {}
    unvisited = dict.fromkeys(G.keys())

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
            cost, to_node = edge

            if cost + shortest_paths[min_node] < shortest_paths[to_node]:
                shortest_paths[to_node] = cost + shortest_paths[min_node]

        del unvisited[min_node]

    return shortest_paths


def main():
    G = make_graph()
    start = 'A'

    shortest_paths = dijkstras(G, start)
    shortest_paths_using_heap = dijkstras_heap(G, start)

    print(f'Shortest path from {start}: {shortest_paths}')
    print(f'Shortest path from {start} using heap: {shortest_paths_using_heap}')


main()
