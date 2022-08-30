## Trees

### B-Trees

* [Playlist](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNFPPv98DjTdD9X6UI9KMHz)
* h/t **Programiz** – [Insertion into a B-tree](https://www.programiz.com/dsa/insertion-into-a-b-tree) | [Deletion from a B-tree](https://www.programiz.com/dsa/deletion-from-a-b-tree)

```
❯ python b_tree.py

--- INSERT & SEARCH ---

Level 0: 2 5 
Level 1: 0 1 
Level 1: 3 4 
Level 1: 6 7 8 9 

2 is in the tree
9 is in the tree
11 is NOT in the tree
4 is in the tree

--- Original B-Tree ---

Level 0: 40 
Level 1: 15 22 30 
Level 2: 1 9 
Level 2: 17 19 21 
Level 2: 23 25 27 
Level 2: 31 32 39 
Level 1: 55 63 
Level 2: 41 47 50 
Level 2: 56 60 
Level 2: 72 90 

--- Case 1: DELETED 21 ---

Level 0: 40 
Level 1: 15 22 30 
Level 2: 1 9 
Level 2: 17 19 
Level 2: 23 25 27 
Level 2: 31 32 39 
Level 1: 55 63 
Level 2: 41 47 50 
Level 2: 56 60 
Level 2: 72 90 

--- Case 2a: DELETED 30 ---

Level 0: 40 
Level 1: 15 22 27 
Level 2: 1 9 
Level 2: 17 19 
Level 2: 23 25 
Level 2: 31 32 39 
Level 1: 55 63 
Level 2: 41 47 50 
Level 2: 56 60 
Level 2: 72 90 

--- Case 2b: DELETED 27 ---

Level 0: 40 
Level 1: 15 22 31 
Level 2: 1 9 
Level 2: 17 19 
Level 2: 23 25 
Level 2: 32 39 
Level 1: 55 63 
Level 2: 41 47 50 
Level 2: 56 60 
Level 2: 72 90 

--- Case 2c: DELETED 22 ---

Level 0: 40 
Level 1: 15 31 
Level 2: 1 9 
Level 2: 17 19 23 25 
Level 2: 32 39 
Level 1: 55 63 
Level 2: 41 47 50 
Level 2: 56 60 
Level 2: 72 90 

--- Case 3b: DELETED 17 ---

Level 0: 15 31 40 55 63 
Level 1: 1 9 
Level 1: 19 23 25 
Level 1: 32 39 
Level 1: 41 47 50 
Level 1: 56 60 
Level 1: 72 90 

--- Case 3a: DELETED 9 ---

Level 0: 19 31 40 55 63 
Level 1: 1 15 
Level 1: 23 25 
Level 1: 32 39 
Level 1: 41 47 50 
Level 1: 56 60 
Level 1: 72 90
```
