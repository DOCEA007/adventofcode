with open("input.txt", 'r') as file:
    data = [[j for j in i.strip()] for i in file.readlines()]
    sum = 0
    for col_i, column in enumerate(data):
        for index, item in enumerate(column):
            if index!=0 and index!=len(column)-1 and col_i!=0 and col_i!=len(data)-1:
                if item == "A":
                    dl = data[col_i+1][index-1]+item+data[col_i-1][index+1]
                    dr = data[col_i+1][index+1]+item+data[col_i-1][index-1]
                    if (dl == "MAS" or dl == "SAM") and (dr == "MAS" or dr == "SAM"):
                        sum+=1
    print(sum)