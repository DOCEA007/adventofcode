with open("input.txt", 'r') as file:
    nums = [list(map(int, line.split())) for line in file]
    left, right = [sorted([num[0] for num in nums]), sorted([num[1] for num in nums])]
    sum = 0
    for i in range(len(left)):
        sum+=abs(left[i]-right[i])
    print(sum)