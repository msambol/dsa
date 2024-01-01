from collections import deque


infinity = float("inf")


def make_graph():
    # identical graph as the YouTube video: https://youtu.be/Tl90tNtKvxs
    return [
            [0, 10, 0, 10, 0, 0],
            [0, 0, 4, 2, 8, 0],
            [0, 0, 0, 0, 0, 10],
            [0, 0, 0, 0, 9, 0],
            [0, 0, 6, 0, 0, 10],
            [0, 0, 0, 0, 0, 0],
        ]


# find paths from source to sink with breadth-first search
def bfs(G, source, sink, parent):
    visited = [False] * len(G)

    queue = deque()
    queue.append(source)

    visited[source] = True
 
    while queue:
        node = queue.popleft()

        for i in range(len(G[node])):
            if visited[i] is False and G[node][i] > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = node
 
    return True if visited[sink] else False


def ford_fulkerson(G, source, sink):
    # This array is filled by breadth-first search (bfs) and stores path
    parent = [-1] * (len(G))
    max_flow = 0

    while bfs(G, source, sink, parent):
        path_flow = infinity
        s = sink
 
        while s != source:
            # Find the minimum value in selected path
            path_flow = min(path_flow, G[parent[s]][s])
            s = parent[s]
 
        max_flow += path_flow
        v = sink
 
        # add or subtract flow based on path
        while v != source:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]

    return max_flow


def main():
    G = make_graph()
    source = 0
    sink = 5
    max_flow = ford_fulkerson(G, source, sink)
    print(f'Maximum flow: {max_flow}')


main()
