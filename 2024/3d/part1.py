import re

def extract_and_multiply(filename):
    total_sum = 0
    pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')

    with open(filename, 'r') as file:
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                num1, num2 = map(int, match)
                total_sum += num1 * num2

    return total_sum

if __name__ == "__main__":
    filename = 'input.txt'
    result = extract_and_multiply(filename)
    print(f"The total sum is: {result}")