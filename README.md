# Project-3-335
Ian Gabriel Vista
vistaiangabriel@csu.fullerton.edu

## To run Exhaustive Search algorithm
Prepare the Grid (F): The grid should be represented as a 2D list, where:

* 'X' indicates an impassable cell (blocked by an opponent).
* '.' indicates a passable cell. The Red Team starts at (0, 0) and aims to reach the goal at (r-1, c-1).
* Define the Function: The soccer_exhaustive function needs to be defined in your Python script or environment.

Run the Function: Pass the grid (F) to the soccer_exhaustive function to calculate the number of valid paths.

## Steps for Dynamic Programming:
Grid Representation (F): Similar to the exhaustive search, the grid will be represented as a 2D list where:

* 'X' indicates an impassable cell (blocked by an opponent).
* '.' indicates a passable cell. The Red Team starts at (0, 0) and aims to reach (r-1, c-1).
Dynamic Programming Matrix (A):

The DP matrix A will store the number of valid paths to each cell.
A[i][j] represents the number of ways to reach the cell (i, j) from the start (0, 0) while avoiding opponents ('X' cells).
Base Case:

If the start (0, 0) is blocked ('X'), return 0 immediately.
Set A[0][0] = 1 as there's only one way to start: standing at (0, 0).
Recurrence Relation:

For each cell (i, j), the number of paths to that cell is the sum of:
The number of paths from the cell above (i-1, j) if that cell is valid and not blocked.
The number of paths from the cell to the left (i, j-1) if that cell is valid and not blocked.
Final Answer:

The number of valid paths to the goal cell (r-1, c-1) will be stored in A[r-1][c-1].
