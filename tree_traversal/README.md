## Tree Traversal

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