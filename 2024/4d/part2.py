# TODO: Finish this
with open("input.txt", 'r') as file:
    data = [[j for j in i.strip()] for i in file.readlines()]
    vertical = list(zip(*data))
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if j==0 or j==len(row)-1:
                