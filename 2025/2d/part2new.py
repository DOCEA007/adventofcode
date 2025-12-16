with open('input.txt', 'r') as file:
    ranges = [i.split('-') for i in file.read().strip().split(',')]
    invalid=[]
    for ids in ranges:
        buffer=''
        for i, num in enumerate(ids[0][:len(ids[0])//2+1]):
            i +=1
            buffer+=num
            print(buffer)
            if buffer*(len(ids[0])//i) >= ids[0] and buffer*(len(ids[0])//i) <= ids[1]:
                print(f'Number {buffer*(len(ids[0])//i)} is zaza')
                invalid.append(int(buffer*(len(ids[0])//i)))
                break







    print(sum(invalid))