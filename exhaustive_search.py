def soccer_exhaustive(grid):
    r, c = len(grid), len(grid[0])
    n = r + c - 2
    counter = 0
    
    # Generate all binary sequences of length n
    for bits in range(2**n):
        candidate = []
        for k in range(n):
            bit = (bits >> k) & 1
            candidate.append((0, 1) if bit == 1 else (1, 0))  # Right (0, 1) or Down (1, 0)
        
        # Validate the candidate path
        i, j = 0, 0
        valid = True
        for move in candidate:
            i, j = i + move[0], j + move[1]
            if i >= r or j >= c or grid[i][j] == 'X':
                valid = False
                break
        if valid and (i, j) == (r-1, c-1):
            counter += 1

    return counter


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
result = soccer_exhaustive(grid)
print("Total valid paths:", result)
