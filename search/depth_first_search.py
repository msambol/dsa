graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}


def dfs(graph, node):
    # The video has visited as an array. I changed this to set because 'n not in visited' is O(1) instead of O(n).
    # See this link for more: https://wiki.python.org/moin/TimeComplexity.
    visited = set()
    stack = []

    visited.add(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = " ")

        # reverse iterate through edge list so results match recursive version
        for n in reversed(graph[s]):
            if n not in visited:
                visited.add(n)
                stack.append(n)


def main():
    dfs(graph, 'A')


main()
