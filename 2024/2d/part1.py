with open("input.txt", "r") as file:
    data = [list(map(int, i.split())) for i in file.read().split("\n")]
    sum = 0
    for report in data:
        if report == sorted(report) or report == sorted(report)[::-1]:
            correct=True
            print(report)
            for i in range(1, len(report)):
                print(report[i])
                diff = abs(report[i]-report[i-1])
                if diff == 1 or diff == 2 or diff == 3:
                    continue
                else:
                    print(abs(report[i]-report[i-1]), " <-")
                    correct=False
        else:
            correct=False
        if correct:
            sum +=1
    print(sum)