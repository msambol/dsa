## Minimum Spanning Trees

[Minimum spanning trees playlist](https://www.youtube.com/playlist?list=PL9xmBV_5YoZObEi3Hf6lmyW-CBfs7nkOV)

### Prim's

* [Video](https://youtu.be/cplfcGZmX7I)
* **Hint:** **P**rim's = **P**ick a node
* h/t **Aladdin Persson** – [GitHub](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/prims/prim_heap.py) | [YouTube](https://www.youtube.com/c/AladdinPersson)

```
❯ python prims.py
Minimum spanning tree: [('A', 'B', 2), ('A', 'C', 3), ('C', 'E', 1), ('A', 'D', 3), ('C', 'F', 6), ('F', 'G', 9)]
Total cost: 24
```

### Kruskal's

* [Video](https://youtu.be/71UQH7Pr9kU)
* **Hint:** Kruskal's = iterate through edges
* h/t **Aladdin Persson** – [GitHub](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kruskal/kruskal_unionfind.py) | [YouTube](https://www.youtube.com/c/AladdinPersson)

```
❯ pip install unionfind
❯ python kruskals.py
Minimum spanning tree: [('C', 'E', 1), ('A', 'B', 2), ('A', 'C', 3), ('A', 'D', 3), ('D', 'F', 7), ('F', 'G', 9)]
Total cost: 25
```
