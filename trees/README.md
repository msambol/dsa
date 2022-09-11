## Trees

### Red-black trees

* [Playlist](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNqDI8qfOZgzbqahCUmUEin)
* Videos: [Intro](https://youtu.be/qvZGUFHWChY) | [Rotations](https://youtu.be/95s3ndZRGbk) | [Insertions (strategy)](https://youtu.be/5IBxA-bZZH8) | [Insertions (examples)](https://youtu.be/A3JZinzkMpk)

```
❯ python red_black_tree.py

-- ROTATIONS VIDEO --
5 2 10 8 12 6 9 

-- After left rotation --
10 5 12 2 8 6 9 

-- After right rotation --
5 2 10 8 12 6 9 

-- INSERTIONS VIDEO, after case 0 --
15(b) 

-- Insert 5 --
15(b) 5(r) 

-- Insert 1 (case 3) --
5(b) 1(r) 15(r) 

-- Move to larger tree --
8(b) 5(b) 15(r) 12(b) 19(b) 9(r) 13(r) 23(r) 

-- Insert 10 (case 1, 2, and 3) --
12(b) 8(r) 15(r) 5(b) 9(b) 13(b) 19(b) 10(r) 23(r) 

-- DELETIONS video --
12(b) 8(r) 15(r) 5(b) 9(b) 13(b) 19(b) 10(r) 23(r) 

-- Delete 19 (case 1) --
12(b) 8(r) 15(r) 5(b) 9(b) 13(b) 23(b) 10(r) 

-- Insert 1 --
12(b) 8(r) 15(r) 5(b) 9(b) 13(b) 23(b) 1(r) 10(r) 

-- Delete 5 (case 2) --
12(b) 8(r) 15(r) 1(b) 9(b) 13(b) 23(b) 10(r) 

-- Delete 12 (case 3) --
13(b) 8(r) 15(b) 1(b) 9(b) 23(r) 10(r) 
```

### B-trees

* [Playlist](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNFPPv98DjTdD9X6UI9KMHz)
* Videos: [Intro](https://youtu.be/FgWbADOG44s) | [Properties](https://youtu.be/fAfuZiFDpRo) | [Search](https://youtu.be/jLEhJqNVauc) | [Insertions](https://youtu.be/tT2DT9Z4H-0) | [Deletions](https://youtu.be/pN4C8cLVc7I)
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
