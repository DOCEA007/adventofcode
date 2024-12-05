import re
with open("input.txt", "r") as file:
    for line in file:
        zaza = re.split(r'don\'t\(\)|do\(\)', line)
        print(line)
        for i,_ in enumerate(zaza):
            if i%2==0:
                print(f"Do: {_}")
            else:
                print(f"Dont: {_}")
    
    # don\'t\(\).+?do\(\)