with open("input.txt", "r") as file:
    data = [list(i) for i in file.read().splitlines()]
    run=True
    while run:
        run=False
        for i_row, col in enumerate(data):
            for i_col, cell in enumerate(col):
                if cell == "^":
                    for i in range(i_row-1, -1, -1):
                        if data[i][i_col] == "#":
                            run=True
                            print("Hit a wall")
                            data[i_row][i_col] = "X"
                            data[i+1][i_col] = ">"
                            break
                        data[i][i_col] = "X"
                elif cell == ">":
                    for i in range(i_col+1, len(col)):
                        if data[i_row][i] == "#":
                            run=True
                            print("Hit a wall")
                            data[i_row][i_col] = "X"
                            data[i_row][i-1] = "v"
                            break
                        data[i_row][i] = "X"
                elif cell == "v":
                    for i in range(i_row+1, len(data)):
                        if data[i][i_col] == "#":
                            run=True
                            print("Hit a wall")
                            data[i_row][i_col] = "X"
                            data[i-1][i_col] = "<"
                            break
                        data[i][i_col] = "X"
                elif cell == "<":
                    for i in range(i_col-1, -1, -1):
                        if data[i_row][i] == "#":
                            run=True
                            print("Hit a wall")
                            data[i_row][i_col] = "X"
                            data[i_row][i+1] = "^"
                            break
                        data[i_row][i] = "X"            
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = data[i][j].replace("<", "X")
            data[i][j] = data[i][j].replace("v", "X")
            data[i][j] = data[i][j].replace(">", "X")
            data[i][j] = data[i][j].replace("^", "X")
    suma=0
    for i in data:
        print("".join(i))
        for j in i:
            if j == "X":
                suma+=1
    print(suma)