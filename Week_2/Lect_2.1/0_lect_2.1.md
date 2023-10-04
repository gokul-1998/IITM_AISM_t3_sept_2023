## State Space Search
![](2023-10-02-09-25-08.png)
![](2023-10-02-09-25-30.png)
- recap , first principles , model based reasoning, and search methods
- ![](2023-10-02-09-26-37.png)
![](2023-10-02-09-27-35.png)
- choose the region that has fewest options first and then color that region
![](2023-10-02-09-29-27.png)
![](2023-10-02-09-30-35.png)
- Constraint Processing, (subsume state space search)   
    - define set of variables
    - describe constraints between subsets of variables 
        - eg countries which are adjacent to each other cannot have the same color
![](2023-10-02-09-35-58.png)
## Some samlple problems
- 
    - map coloring
    - sudoku
    - rubiks cube
    - The water jug problem
        - 3 jugs (8,5,3) litres
    - ![](2023-10-02-09-37-26.png)
    ![](2023-10-02-09-43-31.png)
    ![](2023-10-02-09-45-47.png)    
    - reversible moves are thick lines, the light lines are non reversible
![](2023-10-02-09-47-14.png)
- 8 puzzle -> simpler version of rubik's cube in 2d
![](2023-10-02-09-53-16.png)
![](2023-10-02-09-56-08.png)
![](2023-10-04-18-31-31.png)
- LG is not a good state, as lion and goat cannot be kept together
- GC is also same
![](2023-10-04-18-33-13.png)
![](2023-10-04-18-34-21.png)
- objects on the side where the boat is
- start by telling where boat is 
- here man = boat(right or left)

![](2023-10-04-18-35-39.png)
![](2023-10-04-18-36-27.png)
- here edges represent adjacent countries
- the order is A,B,C...
![](2023-10-04-18-37-39.png)
- solution is the above
- Traveling Salesman - Holy grail of CS
    - order of factorial of N
        - N - no of cities
![](2023-10-04-18-38-41.png)
- figure shows two possible tours
- what is travelling sales man problem?
    - A salesman has to visit a set of cities and return to the starting city, visiting each city exactly once, and minimizing the total distance travelled
- from the picture , the tour on the right looks more optimal
- we will look at it in more detail later, as its an optimization problem and not satisfiability problem
- eg of satisfiability problem is sudoku, where we have to find a solution that satisfies all the constraints 
    - other eg is map coloring
    - other eg is 8 puzzle
    - other eg is water jug problem
    - all the above are satisfiability problems
- a maze is a classic example of a search
- enter and exit are the start and goal states
![](2023-10-04-18-42-03.png)
- we can represent a maze by graph aswell,
- each node is a choice point
- it illustrates an interesting feature of search, we have bird eye view of the maze, but we dont know the details of the maze, this benefit is not availble to the agent
![](2023-10-04-18-44-55.png)
