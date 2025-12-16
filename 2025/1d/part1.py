zeros = 0
def procces_move(moveset, length):
    global index, zeros
    print(f'Current index: {index}')
    print(f'Processing: {moveset}')
    direction, steps = moveset[0], int(moveset[1:])
    index = (index+steps) % length if direction == 'R' else (index-steps) % length
    if index == 0:
        zeros+=1


if __name__ == "__main__":
    index = 50
    with open('input.txt', 'r') as moves:
        for moveset in moves.readlines():
            procces_move(moveset, 100)
        print(f'Finished\nLast index is {index}\nZeros: {zeros}')
    

