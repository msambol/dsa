## Trees

### Traversal

* [Playlist](https://www.youtube.com/playlist?list=PL9xmBV_5YoZO1JC2RgEi04nLy6D-rKk6b)
* Videos: [Pre-order](https://youtu.be/1WxLM2hwL-U) | [In-order](https://youtu.be/5dySuyZf9Qg) | [Post-order](https://youtu.be/4zVdfkpcT6U) | [Level-order](https://youtu.be/IozGo2kwRYE)

```
❯ python traversal.py
 
                1
        2               3
    4      5        6       7  
   8 9   10 11    12 13   14 15
        
--- LEVEL ORDER iterative ---
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

--- PRE-ORDER iterative ---
1 2 4 8 9 5 10 11 3 6 12 13 7 14 15 

--- PRE-ORDER recursive ---
1 2 4 8 9 5 10 11 3 6 12 13 7 14 15 

--- IN-ORDER iterative ---
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15 

--- IN-ORDER recursive ---
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15 

--- POST-ORDER recursive ---
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1 
```

### B-Trees

* [Playlist](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNFPPv98DjTdD9X6UI9KMHz)
* Videos: [Intro](https://youtu.be/FgWbADOG44s) | [Properties](https://youtu.be/fAfuZiFDpRo) | [Search](https://youtu.be/jLEhJqNVauc) | [Insertions](https://youtu.be/tT2DT9Z4H-0) | [Deletions]()
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
