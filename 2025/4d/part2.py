def return_adj(row, column):
    adj=0
    for cr in (-1,0,1):
        for cc in (-1,0,1):
            if cc==0 and cr==0:
                continue
            if 0<=row+cr<len(grid) and 0<=column+cc<len(grid[0]):
                if grid[row+cr][column+cc]=="@":
                    adj+=1
    return adj


with open('input.txt', 'r') as file:
    rolls=0
    grid = [i.strip() for i in file]
    final_grid=grid[:]
    for i in grid:
        print(i)
    while True:
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column]=="@":
                    adj = return_adj(row, column)
                    if adj<4:
                        rolls+=1
                        final_grid[row]=final_grid[row][:column]+"X"+final_grid[row][column+1:]
                elif grid[row][column]=='X':
                    final_grid[row]=final_grid[row][:column]+"."+final_grid[row][column+1:]
        print(rolls)
        for i in final_grid:
            print(i)
        if grid==final_grid:
            break
        else:  
            grid=final_grid[:]

    