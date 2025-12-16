def printm(matrix):
    for i in matrix:
        print(i)
with open('input.txt', 'r') as file:
    lines = file.readlines()
    data = [''.join(i) for i in list(zip(*[i for i in lines]))]
    calcs, current, evals = [], [], []
    for item in data:
        if item.strip() == '':
            calcs.append(current)
            current=[]
        else:
            current.append(item)
    if current:
        calcs.append(current)
    for calc in calcs:
        expression=(calc[0]+calc[0][-1].join(list(calc[1:]))).replace(' ', '')
        evals.append(eval(expression)) 
    print(sum(evals))
    