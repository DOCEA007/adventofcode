def printm(matrix):
    for i in matrix:
        print(i)
with open('input.txt', 'r') as file:
    matrix = list(zip(*[i.strip().split() for i in file.readlines()]))
    expressions = [expression[-1].join(expression[:-1]) for expression in matrix]
    results=[eval(i)for i in expressions]
    print(results)
    print(sum(results))

    