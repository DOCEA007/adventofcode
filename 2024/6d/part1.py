def rotate(matrix):
    return list(list(x) for x in zip(*matrix))[::-1]
def rotate_coordinates(x, y, n):
    # Rotate coordinates 90 degrees counterclockwise n times
    for _ in range(n):
        x, y = y, -x
    return x, y
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
    while sus:
        printm(data)       
        for i_row in range(1, rows):
            for i_col in range(cols):
                if data[i_row][i_col] == "^":
                    # Check above for a #
                    moved = False
                    for k in range(i_row - 1, -1, -1):
                        # print(k)
                        original_k, original_i_col = rotate_coordinates(k, i_col, rotations)
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