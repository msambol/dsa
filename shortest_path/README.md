## Shortest Path Algos

[Shortest path algos playlist](https://www.youtube.com/playlist?list=PL9xmBV_5YoZO-Y-H3xIC9DGSfVYJng9Yw)

### Dijkstra's

* [Video](https://youtu.be/_lHSawdgXpI)
* Note: shortest path from one node to all nodes
* h/t **Aladdin Persson** – [GitHub](https://github.com/aladdinpersson/Algorithms-Collection-Python/tree/master/Algorithms/graphtheory/dijkstra) | [YouTube](https://www.youtube.com/c/AladdinPersson)

```
❯ python dijkstras.py
Shortest path from A: {'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}
Shortest path from A using heap: {'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}
```

### Bellman-Ford

* Videos: [Theory](https://youtu.be/9PHkk0UavIM) | [Example](https://youtu.be/obWXjtg0L64)
* Note: shortest path from one node to all nodes, negative edges allowed

```
❯ python bellman_ford.py
Shortest path from S: {'S': 0, 'A': 5, 'B': 5, 'C': 7, 'D': 9, 'E': 8}
```

### Floyd-Warshall

* [Video](https://youtu.be/4OQeCuLYj-4)
* Note: shortest path between all pairs of vertices, negative edges allowed

```
❯ python floyd_warshall.py
Shortest path matrix:

[0, -1, -2, 0]
[4, 0, 2, 4]
[5, 1, 0, 2]
[3, -1, 1, 0]
```
