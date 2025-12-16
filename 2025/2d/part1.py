with open('input.txt', 'r') as file:
    ranges = [i.split('-') for i in file.read().strip().split(',')]
    invalid=[]
    for ids in ranges:
        for i in range(int(ids[0]), int(ids[1])):
            i = str(i)
            if i[len(i)] == i[:len(i)//2]:
                invalid.append(int(i))
    print(sum(invalid))