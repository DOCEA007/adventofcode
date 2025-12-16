with open('input.txt', 'r') as file:
    suma=0
    for battery in [i.strip() for i in file]:
        maxi = 0
        for index1, i in enumerate(battery):
            for j in battery[index1+1:]:
                maxi = int(i+j) if int(i+j)>=maxi else maxi
        suma+=maxi
    print(suma)