## Depth First Iterative Deepening

- we use heuristic search,
![](2023-10-05-09-12-31.png)
- we want to looks at an algo that uses both the good properties from both the algos,i.e
    - linear space for open
    - shortest path delivery

- we shall start by Depth bounded DFS(DBDFS)
    - it means we are guaranteeing linear space
    - lets say the bound is d
![](2023-10-05-09-15-30.png)
![](2023-10-05-09-15-46.png)
- not different from earlier DFS
- here instead of node pair, we have a node triple
![](2023-10-05-09-17-41.png)
![](2023-10-05-09-17-54.png)
![](2023-10-05-09-19-17.png)
![](2023-10-05-09-19-33.png)
- it increasingly looks at  , increasing depth bounds
- we initialize count to -1
- iteratively increase the depth bound,
![](2023-10-05-09-22-46.png)
https://youtu.be/QuG7ooEPOFI?t=748
![](2023-10-05-09-25-27.png)
- ![](2023-10-05-09-27-09.png)
- because D is already in closed, DFID will miss finding the shortest path
![](2023-10-05-09-29-33.png)
![](2023-10-05-21-22-59.png)
- chess players think 6 moves ahead or 8 moves ahead. 
- this is called ply
- instead of keeping this depth constant, we can increase it by 1   
- DFID enable any time move generations, in games like chess
![](2023-10-05-23-26-57.png)
![](2023-10-05-23-27-28.png)
- is there a catch?
    - what is the extra cost?
![](2023-10-05-23-28-57.png)
![](2023-10-05-23-30-24.png)
- this is the number of leaves in the full tree, 
- extra work , ratio is 
![](2023-10-05-23-31-25.png)

![](2023-10-05-23-32-58.png)    
![](2023-10-05-23-33-11.png)
- this is not a good strategy
![](2023-10-05-23-33-41.png)
- the three algos are blind or uninformed search
    - BFS
    - DFS
    - DFID
- blind means, when we are searching, we are not using any information about the goal, we are not aware where the goal is hence called uninformed
- A good search Algo should have some sense of direction, it should be informed, it should use some information about the goal
    - its should have some sense of direction, it should realize that it is going in the wrong direction, and it should change direction

## heuristic search- NEXT