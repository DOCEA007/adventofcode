import re

def extract_and_multiply(filename):
    total_sum = 0
    pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')
    pattern_check = re.compile(r'(don\'t\(\))|(do\(\))')

    with open(filename, 'r') as file:
        for line in file:
            print(line)
            splited = [x for x in re.split(pattern_check, line) if x is not None]
            print(splited)
            for index in range(len(splited)):
                if index == 0 or index!=0 and splited[index-1] == "do()":
                    matches = pattern.findall(splited[index])
                    for match in matches:
                        num1, num2 = map(int, match)
                        total_sum += num1*num2
    return total_sum    

if __name__ == "__main__":
    filename = 'input.txt'
    result = extract_and_multiply(filename)
    print(f"The total sum is: {result}")    