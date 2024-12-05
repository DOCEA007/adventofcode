def remove_item(lst, index):
    return lst[:index] + lst[index+1:]

def validate(a, b, increasing):
    if increasing:
        return b > a and (b - a) <= 3
    else:
        return b < a and (a - b) <= 3

def analyze(elements):
    # Determine trend and validate the sequence
    increasing = elements[0] < elements[1]  # Initial trend
    for i in range(1, len(elements)):
        if not validate(elements[i-1], elements[i], increasing):
            return False
    return True

def compute(report):
    if analyze(report):  # Check the original sequence
        return True
    for i in range(len(report)):  # Try removing each element once
        new_report = remove_item(report, i)
        if analyze(new_report):
            return True
    return False

with open("input.txt", "r") as file:
    data = [list(map(int, line.split())) for line in file.read().split("\n") if line]
    total = 0
    for report in data:
        if compute(report):
            total += 1
    print(total)
