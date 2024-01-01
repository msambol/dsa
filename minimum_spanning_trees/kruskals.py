from unionfind import unionfind


def make_graph():
    # identical graph as the YouTube video: https://youtu.be/71UQH7Pr9kU
    # tuple = (cost, n1, n2)
    return {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }


def load_edges(G):
    num_nodes = 0
    edges = []

    for _, value in G.items(): 
        num_nodes += 1
        edges.extend(value)

    return num_nodes, sorted(edges)


# HACKY: unionfind only works with numbers not letters.
# I converted the letter to an int with 'ord' and then subtracted 65 since 'A' = 65.
def conv_char(c):
    return ord(c) - 65


def kruskals(G):
    total_cost = 0
    MST = []

    num_nodes, edges = load_edges(G)
    uf = unionfind(num_nodes)

    for edge in edges:
        cost, n1, n2 = edge[0], edge[1], edge[2]

        if not uf.issame(conv_char(n1), conv_char(n2)):
            total_cost += cost
            uf.unite(conv_char(n1), conv_char(n2))
            MST.append((n1, n2, cost))

    return MST, total_cost


def main():
    G = make_graph()
    MST, total_cost = kruskals(G)

    print(f'Minimum spanning tree: {MST}')
    print(f'Total cost: {total_cost}')


main()
