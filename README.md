# **AI Sudoku Solver** 


**AI Sudoku Solver**

The goal of this project is the following:
* Build an intelligent agent that will solve every sudoku 



[//]: # (Image References)

[image1]: ./images/sudoku-easy.png "sudoku easy"
[image2]: ./images/easy-solution.png "sudoku easy solution"
[image3]: ./images/harder-sudoku-reduced.png "sudoku hard reduction"

---

### Reflection

### 1. What is Sudoku?

Sudoku is one of the world's most popular puzzles. It consists of a 9x9 grid, and the objective is to fill the grid with digits in such a way that each row, each column, and each of the 9 principal 3x3 subsquares contains all of the digits from 1 to 9.
The puzzle is given as a partially completed grid, and the goal is to fill in the missing numbers. Below is an example of such a grid.

![alt text][image1]

Naming Convention:

* The rows will be labelled by the letters A, B, C, D, E, F, G, H, I.
* The columns will be labelled by the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9.
* The individual squares at the intersection of rows and columns will be called `boxes`. These boxes will have labels 'A1', 'A2', …, 'I9'.
* The complete rows, columns, and 3x3 squares, will be called `units`. Thus, each unit is a set of 9 boxes, and there are 27 units in total.
* For a particular box (such as 'A1'), its `peers` will be all other boxes that belong to a common unit (namely, those that belong to the same row, column, or 3x3 square).


### 2. Pipeline Description.

Two powerful techniques that are used throughout the field of AI are used:

* Constraint Propagation

In constraint propagation, two strategies are used in my code. They are `Elimination` and `Only_choice`. Iterating throw them helps optimize the solution  and provide us with an answer to the sudoku.

for the easy sudoku problem shown above, the code provides the correct solution which can be seen here:

![alt text][image2]

When using the reduction method on a harder sudoku, the following answer is given:

![alt text][image3]

The constraint propagation technique is not enough to solve it. Hence the need for the third strategy which is the `search` technique

* Search


