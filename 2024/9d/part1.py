def move(inp):
    visual = list(inp)
    for last in range(len(visual)-1, 0, -1):
        for first in range(len(visual)):
            if visual[first] == ".":
                visual[first] = visual[last]
                visual[last] = "."
    return visual
with open("input.txt", "r") as file:
    data = file.read()
    visual=''
    file_id = 0

    for i in range(len(data)):  
        if i%2==0:
            for i in range(int(data[i])):
                visual+=str(i)
        else:
            visual+=int(data[i])*"."
    result = list(filter(lambda a: a!=".", move(visual)))
    print(result)
    checksum = 0
    for i, value in enumerate(result):
        checksum += int(value)*i
    print(checksum)

with open("output.txt", "w+") as file:
    file.write(str(checksum))