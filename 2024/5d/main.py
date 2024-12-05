from collections import defaultdict
with open("input.txt", "r") as f:
    rules = defaultdict(list)
    data = [i.split() for i in f.read().split("\n\n")]
    [rules[key].append(value) for key, value in (map(int,j.split("|")) for j in data[0])]
    rules = dict(rules)
    updates = data[1]
    print(rules)
    # key by value in list: list([i for i in rules if search in rules[i]])
    