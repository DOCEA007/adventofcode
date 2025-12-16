class box:
    def __init__(self, data):
        self.data = data
        self.next = None 

with open('input.txt', 'r') as file:
    boxes = [box(list(map(int, i.split(',')))) for i in file.readlines()]
    