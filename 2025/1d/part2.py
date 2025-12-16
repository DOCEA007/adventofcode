zeros = 0
def procces_move(moveset, length):
    global index, zeros
    old_zero = zeros
    direction, steps = moveset[0], int(moveset[1:])
    if direction == 'R':
        first = length if index == 0 else length - index
    else: 
        first = length if index == 0 else index
    if steps >= first:
        hits_this_move = 1 + (steps - first) // length
        zeros += hits_this_move
    index = (index+steps) % length if direction == 'R' else (index-steps) % length
    print(f'The dial is rotated {moveset} to point at {index}')
    if old_zero != zeros:
        print(f'Added zero at move: {moveset}')


if __name__ == "__main__":
    with open('input.txt', 'r') as moves:

        index = 50
        print(f'The dial starts by pointing at {index}.')
        for moveset in moves.readlines():
            procces_move(moveset.strip(), 100)
        print(f'Finished\nLast index is {index}\nZeros: {zeros}')
    

