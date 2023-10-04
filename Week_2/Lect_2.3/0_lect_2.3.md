 ## Planning Problems, Configuration Problems

 - There are two kinds of problems,that we can solve using our state space search
    - Planning Problems
        - ![](2023-10-04-19-49-27.png)
    - Configuration Problems
        - a state satisfying a description of the goal is solved
        - eg : N-queens problem(give me a configuration of queens on a chess board such that no queen can attack any other queen)
        - SAT - satisfiability problem, given a boolean expression, find an assignment of true and false to the variables in the expression such that the expression evaluates to true
        - Hamiltonian path problem, given a graph, find a path that visits every node exactly once
        - ![](2023-10-04-19-48-57.png)

- ![](2023-10-04-19-52-08.png)
    - state space is on the right
    - the search space is generated on the fly
    ![](2023-10-04-19-53-42.png)
![](2023-10-04-19-54-56.png)
- parent of D is A
![](2023-10-04-19-57-07.png)
- so far we did , non deterministic method(pick some node N from open)
    - non deterministic means ,we dont specify which node to pick 
- Not non-deterministic means somehow the algo knows what is the correct choice
    - for eg , when we study non-deterministic finite automata, we assume that there is an oracle which know which is the right choice
![](2023-10-04-21-24-01.png)
- we used set so for, now we shall use list
![](2023-10-04-21-25-02.png)
![](2023-10-04-21-25-12.png)
- : here means , add an element to the head of the list 
![](2023-10-04-21-26-50.png)
![](2023-10-04-21-27-05.png)
- this means we started with list1, we added a new element to the head of the list, to arrive at list2, its like assignment operator
![](2023-10-04-21-28-05.png)
- these are equivalent
- ![](2023-10-04-21-29-27.png)
https://youtu.be/fTPrAci0WWA?t=653
- basically he is saying tail[1]=[]
![](2023-10-04-21-30-07.png)
- tail is basically, everything except head
![](2023-10-04-21-31-01.png)
- `:` operation is specifically used to add an element to a list
- `++` - take two lists and add them together, 
- ![](2023-10-04-21-33-56.png)
    - here this treats the first argument as an element
- ![](2023-10-04-21-34-40.png)
- ![](2023-10-04-21-36-12.png)
    - the `_` means we dont care about the second element
- we can access the first element of the tuple using  a function called first
- ![](2023-10-04-21-37-17.png)
    - 8th point says we can have any datatype
    - 9th point is an assignment
    - 10th point is a test, it will return true or false
- ![](2023-10-04-21-38-48.png)
![](2023-10-04-21-41-28.png)
- here there are three elements in the tuple,
- (a,head:tail,c)