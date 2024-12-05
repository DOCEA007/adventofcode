from collections import defaultdict
with open("input.txt", "r") as f:
    rules = defaultdict(list)
    data = [i.split() for i in f.read().split("\n\n")]
    [rules[key].append(value) for key, value in (map(int,j.split("|")) for j in data[0])]
    rules = dict(rules)
    updates = [list(map(int, i.split(","))) for i in data[1]]
    valids = []
    for update in updates:
        print(update)
        valid = True
        for index, item in enumerate(update):
            if item in rules:
                if not bool(set(update[:index]) & set(rules[item])):
                    valid = False
            if not bool(set(update[index-1:]) & set([i for i in rules if item in rules[i]])):
                valid = False
        if valid:
            valids.append(update)
    print(valids) 
            
    # key by value in list: list([i for i in rules if search in rules[i]])
    