from collections import deque


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}


def bfs(graph, node):
    # The video has visited as an array. I changed this to set because 'n not in visited' below is O(1) instead of O(n).
    # See this link for more: https://wiki.python.org/moin/TimeComplexity.
    visited = set()
    # The video has queue as an array. I changed this to deque because popping the first element is O(1) instead of O(n).
    # See this link for more: https://wiki.python.org/moin/TimeComplexity.
    queue = deque()

    visited.add(node)
    queue.append(node)

    while queue:
        # popleft is O(1). For an array, pop(0) is O(n). Hence the change to deque from array.
        s = queue.popleft()
        print(s, end = ' ')

        for n in graph[s]:
            # Because visited is a set, this lookup is O(1).
            if n not in visited:
                visited.add(n)
                queue.append(n)


def main():
    bfs(graph, 'A')


main()
