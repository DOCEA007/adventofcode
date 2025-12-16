with open('input.txt', 'r') as file:
    ranges = [i.split('-') for i in file.read().strip().split(',')]
    invalid=[]
    for ids in ranges:
        for ID in range(int(ids[0]), int(ids[1])+1):
            ID = str(ID)
            for prime in [2,3,5,6,11,17]:
                    if len(ID)%prime==0:
                        parts = [ID[i:i+len(ID)//prime] for i in range(0, len(ID), len(ID)//prime)] 
                        print(parts)
                        if len(set(parts)) == 1:
                            invalid.append(int(ID))
                            print(ID)
                            break
    print(sum(invalid))