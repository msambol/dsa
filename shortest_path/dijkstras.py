infinity = float("inf")

def make_graph():
    # identical graph from the YouTube video: https://youtu.be/_lHSawdgXpI
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
    visited = {} 
    history = {} 
    heap = [] 
    path = []

    for node in list(G.keys()):
        shortest_paths[node] = infinity
        visited[node] = False

    shortest_paths[start] = 0 
    visited[start] = True

    heapq.heappush(heap, (0, start))

    while heap:
        (distance, node) = heapq.heappop(heap)
        visited[node] = True

        for edge in G[node]:
            cost = edge[0]
            to_node = edge[1]

            if (not visited[to_node]) and (distance + cost < shortest_paths[to_node]):
                shortest_paths[to_node] = distance + cost
                heapq.heappush(heap, (shortest_paths[to_node], to_node))

    return shortest_paths


def dijkstras(G, start='A'):
    shortest_paths = {}
    unvisited = list(G.keys())

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
    shortest_paths_using_heap = dijkstras(G, start)

    print(f'Shortest path from {start}: {shortest_paths}')
    print(f'Shortest path from {start} using heap: {shortest_paths}')

main()
