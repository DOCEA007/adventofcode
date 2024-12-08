with open("input.txt", "r") as f:
    data = [i.split() for i in f.read().split("\n\n")]
    rules = [list(map(int, i.split("|"))) for i in data[0]]
    updates = [list(map(int, i.split(","))) for i in data[1]]
    invalids = []
    def is_valid_order(update):
        for i in range(len(update) - 1):
            for rule in rules:
                if update[i] == rule[1] and update[i + 1] == rule[0]:
                    return False
        return True
    def reorder_update(update):

        n = len(update)
        for i in range(n):
            for j in range(n - 1):
                for rule in rules:
                    if update[j] == rule[1] and update[j + 1] == rule[0]:
                        update[j], update[j + 1] = update[j + 1], update[j]
        return update
    for update in updates:
        if not is_valid_order(update):
            invalids.append(reorder_update(update))
    middle_sum = sum(update[len(update) // 2] for update in invalids)
    print(middle_sum)