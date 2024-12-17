def rotate(matrix):
    return list(list(x) for x in zip(*matrix))[::-1]
def rotate_coordinates(x, y, row, n):
    new_x = x
    new_y = y
    for _ in range(n):
        new_x, new_y = len(row)-1-new_y, new_x
    return new_x,new_y


    
def step(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i_row in range(1, rows):
        for i_col in range(cols):
            if matrix[i_row][i_col] == "^":
                # Check above for a #
                for k in range(i_row - 1, -1, -1):
                    if matrix[k][i_col] == "#":
                        # Move ^ to the position just below #
                        matrix[i_row][i_col] = "."
                        matrix[k + 1][i_col] = "^"
                        break

def printm(matrix):
    for row in matrix:
        print(" ".join(row))
    print("=====================")

with open("input.txt") as f:
    lines = f.readlines()
    data = [list(x.strip()) for x in lines]
    rows = len(data)
    cols = len(data[0])
    rotations = 0
    sus = True
    visited = set()
    visited.add("s")
    while sus:
        printm(data)       
        for i_row in range(1, rows):
            for i_col in range(cols):
                if data[i_row][i_col] == "^":
                    # Check above for a #
                    moved = False
                    for k in range(i_row - 1, -1, -1):
                        # print(k)
                        original_k, original_i_col = rotate_coordinates(k, i_col,data[i_row],  rotations)
                        visited.add((original_k, original_i_col))
                        if data[k][i_col] == "#":
                            # Move ^ to the position just below #
                            data[i_row][i_col] = "."
                            data[k + 1][i_col] = "^"
                            moved = True
                            break

                    if not moved:
                        # Move ^ to the top row
                        data[i_row][i_col] = "."
                        data[0][i_col] = "^"
                        for i in range(i_row, 0, -1):
                            visited.add((i, i_col))
                        sus = False
                        print("ZAZAAAA")
        
        printm(data)
        visited.pop()
        if sus:
            data = rotate(data)
            rotations = (rotations + 1) % 4
            printm(data)
            
            print("Steps: ", len(visited))
    print(len(visited))


# Function to print the matrix
def print_colored_matrix(matrix, highlight_indices, color="\033[91m"):  # Default red color
    reset = "\033[0m"  # Reset color
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if (i, j) in highlight_indices:
                # Print highlighted item
                print(f"{color}{item}{reset}", end=" ")
            else:
                # Print normal item
                print(item, end=" ")
        print()  # Newline after each row

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Example set of indices to highlight
highlight_indices = {(0, 0), (1, 1), (2, 2)}  # Highlight diagonal elements

# Call the functiona
data= rotate(data)
data=rotate(data)

print_colored_matrix(data, visited)
