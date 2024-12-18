def soccer_dyn_prog(grid):
    r, c = len(grid), len(grid[0])
    if grid[0][0] == 'X':
        return 0

    # Initialize DP table
    dp = [[0] * c for _ in range(r)]
    dp[0][0] = 1

    # Fill the table
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'X':
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    return dp[r-1][c-1]


# Prompt the user for the grid dimensions
r = int(input("Enter the number of rows in the grid: "))
c = int(input("Enter the number of columns in the grid: "))

# Prompt the user to enter the grid itself
grid = []
print(f"Enter the grid with {r} rows, using '0' for open spaces and 'X' for obstacles:")
for i in range(r):
    while True:
        row = input(f"Row {i+1}: ").split()
        if len(row) != c:
            print(f"Error: Each row must have {c} values.")
        else:
            grid.append(row)
            break

# Call the function with the user input
result = soccer_dyn_prog(grid)
print("Total number of unique paths:", result)
