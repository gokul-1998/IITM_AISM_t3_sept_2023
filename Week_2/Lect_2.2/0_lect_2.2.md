## General Search Algorithms

- we want to do domain independent problem solving algorithms
![](2023-10-04-18-48-53.png)
- the task is to develop those algos
![](2023-10-04-18-49-22.png)
- we want to reach the goal state from the start state
- the state space search is implicit, the graph is not given to us,we have to generate the graph on the fly using the movegen function
- we are only given start and the goal state, sometimes, only the start state and the goal description, eg, Water jug problem
    - we had three , different goal states in which we can measure goal states
![](2023-10-04-18-52-29.png)
![](2023-10-04-18-52-38.png)
![](2023-10-04-18-52-51.png)
![](2023-10-04-18-53-22.png)
- goal test is to check if the current state is the goal state or not 
![](2023-10-04-18-54-58.png)
![](2023-10-04-18-55-17.png)
![](2023-10-04-18-55-35.png)
    - purple - open,
    - dark - closed

![](2023-10-04-18-56-22.png)
![](2023-10-04-18-57-09.png)
![](2023-10-04-18-58-36.png)
![](2023-10-04-19-23-24.png)
- Here is our simple search algo
    - we start by adding S to open
```
Open= {S}
while open:
    N=open[0]
    open.remove(N) 
    if goaltest(N)==True:
        return N
    else:
        # we call the move gen function to generate the children of N, and add those to open
        open=movegen(N,open) 
return Failure
```

- we do this if we get goal ,or if open has no more nodes by returning failure

- in search tree it is possible to have cycles, but in search graph, we cannot have cycles
![](2023-10-04-19-30-18.png)
![](2023-10-04-19-30-39.png)
```
Open= {S}
Closed={}
while open:
    N=open[0]
    open.remove(N) 
    closed.add(N)
    if goaltest(N)==True:
        return N
    else:
        # we call the move gen function to generate the children of N, and add those to open
        open=movegen(N,open) - closed
return Failure
```
- the search space is smaller than the previous one
![](2023-10-04-19-34-37.png)
- here if we can see there is D,B,C that is left in white , as they are already in closed,
- we shall see later if ther is any hidden cost.
- ![](2023-10-04-19-36-54.png)
https://youtu.be/nxeoZkr0k6U?t=862
- we will only add new nodes, 
- start with s,  add A,B,C to open
- we will not add B to child of A, 
    - because S is already in closed
    - A has 3 children (SBD)
    - B is already in open , so we will not add it
    - so we will go with D
![](2023-10-04-19-40-39.png)     
![](2023-10-04-19-40-52.png)
- this algo says only if you can reach the goal, it wont give you the path
![](2023-10-04-19-42-11.png)