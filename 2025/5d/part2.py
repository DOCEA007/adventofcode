with open('input.txt', 'r') as file:
    file = file.read()
    ranges = [list(map(int,j)) for j in [i.split('-') for i in file.split('\n\n')[0].split()]]
    ids = list(map(int,file.split('\n\n')[1].split()))
    valids=set()
    for Range in ranges:
        count,i = Range[1]-Range[0]+1,0

        while i!=count:
            valids.add(Range[1]-i)
            i+=1
        
    print(len(valids))