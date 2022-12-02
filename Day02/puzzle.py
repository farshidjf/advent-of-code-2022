to_num = lambda a, x: (ord(a) - ord('A'), ord(x) - ord('X'))
correct = lambda a, x: (a, (a + x - 1) % 3)  # correction for puzzle 2
score = lambda a, x: (x + 1) + ((x - a + 1) % 3) * 3
        
file_name = 'Day02/input.txt'
with open(file_name) as input_file:
    rounds = [to_num(*(line.split())) for line in input_file.readlines()]
    print(f'puzzle 1: {sum([score(*round) for round in rounds])}')
    print(f'puzzle 2: {sum([score(*correct(*round)) for round in rounds])}')