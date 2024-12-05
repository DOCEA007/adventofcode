with open("input.txt", 'r') as file:
    nums = [list(map(int, line.split())) for line in file]
    left = sorted(list(map(int, [num[0] for num in nums])))
    right = sorted(list(map(int, [num[1] for num in nums])))
    print(left, right)
    sum=0
    for i in range(len(left)):
        doubles = len([item for item in right if item==left[i]])
        sum+=doubles*left[i]
    print(sum)