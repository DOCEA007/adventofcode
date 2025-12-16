index = 50
zeros = 0
with open('input.txt', 'r') as moves:
    for moveset in moves.readlines():
        direction, steps = moveset[0], int(moveset[1:])
        index = (index+steps) % 100 if direction == 'R' else (index-steps) % 100
        if index == 0:
            zeros+=1
    print(f'Finished\nLast index is {index}\nZeros: {zeros}')


