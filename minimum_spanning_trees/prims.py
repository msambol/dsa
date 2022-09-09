import heapq

def make_graph():
    # identical graph as the YouTube video: https://youtu.be/cplfcGZmX7I
    # tuple = (cost, n1, n2)
    return {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }


def prims(G, start='A'):
    unvisited = list(G.keys())
    visited = []
    total_cost = 0
    MST = []

    unvisited.remove(start)
    visited.append(start)

    heap = G[start]
    heapq.heapify(heap)

    while unvisited:
        (cost, n2, n1) = heapq.heappop(heap)
        new_node = None

        if n1 in unvisited and n2 in visited:
            new_node = n1
            MST.append((n2, n1, cost))

        elif n1 in visited and n2 in unvisited:
            new_node = n2
            MST.append((n1, n2, cost))

        if new_node != None:
            unvisited.remove(new_node)
            visited.append(new_node)
            total_cost += cost

            for node in G[new_node]:
                heapq.heappush(heap, node)

    return MST, total_cost


def main():
    G = make_graph()
    MST, total_cost = prims(G, 'A')

    print(f'Minimum spanning tree: {MST}')
    print(f'Total cost: {total_cost}')

main()
