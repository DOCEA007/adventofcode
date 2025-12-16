def solve(battery, count):
    start, num=0,0
    row = [int(i) for i in battery]
    for i in range(count):
        end = len(row)-(count-i)+1
        maxi = max(row[start:end])
        start = row.index(maxi,start,end)+1
        num=num*10+maxi
    return num

with open('input.txt', 'r') as file:
    suma=0
    for battery in [i.strip() for i in file]:
        suma += solve(battery, 12)
    print(suma)
