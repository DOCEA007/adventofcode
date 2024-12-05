with open("input.txt", 'r') as file:
    search = "XMAS"
    sum=0
    data = [[j for j in i.strip()] for i in file.readlines()]
    vertical = list(zip(*data))
    for row in data:
        sum+="".join(row).count(search)
        sum+="".join(reversed(row)).count(search)
    for row in vertical:
        sum+="".join(row).count(search)
        sum+="".join(reversed(row)).count(search)
    max_row = len(data)
    max_col = len(data[0])
    min_bdiag = -max_row + 1
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y].append(data[y][x])
            bdiag[x-y-min_bdiag].append(data[y][x])
    for diagonal in fdiag:
        sum+="".join(diagonal).count(search)
        sum+="".join(reversed(diagonal)).count(search)
    for diagonal in bdiag:
        sum+="".join(diagonal).count(search)
        sum+="".join(reversed(diagonal)).count(search)
    print(sum)