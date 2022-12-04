file_name = 'Day04/input.txt'
with open(file_name) as input_file:
    pairs = [[[int(i) for i in pair.split('-')] for pair in line.strip().split(',')] for line in input_file]

set_pairs = [[set(range(r1[0], r1[1] + 1)), set(range(r2[0], r2[1] + 1))] for r1, r2 in pairs]

print(f'puzzle 1: {sum([task1 <= task2 or task2 <= task1 for task1, task2 in set_pairs])}')
print(f'puzzle 2: {sum([task1 & task2 != set() for task1, task2 in set_pairs])}')