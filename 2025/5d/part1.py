with open('input.txt', 'r') as file:
    file = file.read()
    ranges = [list(map(int,j)) for j in [i.split('-') for i in file.split('\n\n')[0].split()]]
    ids = list(map(int,file.split('\n\n')[1].split()))
    valids=0
    for Id in ids:
        for Range in ranges:
            if Id >=Range[0] and Id <= Range[1]:
                valids+=1
                break
    print(valids)