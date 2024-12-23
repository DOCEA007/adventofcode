with open("input.txt", 'r') as f:
    data = [list(i) for i in f.read().strip().split("\n")]
    max_row = len(data)
    max_col = len(data[0])
    min_bdiag = -max_row + 1
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y].append(data[y][x])
            bdiag[x-y-min_bdiag].append(data[y][x])
    