from collections import defaultdict
with open("input.txt", "r") as f:
    data = [i.split() for i in f.read().split("\n\n")]
    rules = [list(map(int, i.split("|"))) for i in data[0]]
    updates = [list(map(int, i.split(","))) for i in data[1]]
    valids = []
    for update in updates:
        valid=True
        for index, item in enumerate(update):
            needed=[x for x in rules if item in x]
            before = update[:index]
            if before!=[]:
                for index2, last in enumerate(before):
                    for i in needed:
                        if last == i[0]:
                            if index2>index:
                                valid=False
                                break
                        if last == i[1]:
                            if index2<index:
                                valid=False
                                break 
        if valid:
            valids.append(update)
    print(sum([i[len(i)//2] for i in valids]))

    
    
    
    
    
    
    
    
    
    # for update in updates:
    #     print(update)
    #     valid = True
    #     for index, item in enumerate(update):
    #         if item in rules:
    #             if not bool(set(update[:index]) & set(rules[item])):
    #                 valid = False
    #         if not bool(set(update[index-1:]) & set([i for i in rules if item in rules[i]])):
    #             valid = False
    #     if valid:
    #         valids.append(update)
    # print(valids) 
            
    # key by value in list: list([i for i in rules if search in rules[i]])
    