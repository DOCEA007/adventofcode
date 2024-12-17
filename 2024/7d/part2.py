import itertools
def generate_combinations(nums):
    nums.append("")
    n = len(nums)-2
    combinations = [list(tup) for tup in itertools.product('*+|', repeat=n)]
    final=[]
    for item in combinations:
        item.append('')
        output=[]
        for i in range(n+1):
            output.append(nums[i])
            output.append(item[i])
        final.append(output[:-1])

    return final

with open('input.txt', 'r') as file:
    n = [item.split(': ') for item in file.read().split('\n')]
    # print(n)
    valid = set()
    for line in n:
        value = int(line[0])
        nums = line[1].split(' ')
        for comb in generate_combinations(nums):
            result = comb[0]
            for i in range(1, len(comb), 2):
                operator, num = comb[i], int(comb[i+1])
                if operator=='|':
                    result = int(f"{result}{num}")
                else:
                    result = eval(f"{result}{operator}{num}")
            if result == value:
                print(f"{' '.join(comb)} = {value}")
                valid.add((tuple(nums), value))
    sum=0
    for i in valid:
        sum+=i[1]
    print(sum)