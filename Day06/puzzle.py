
file_name = 'Day06/input.txt'
with open(file_name) as input_file:
    data_stream = input_file.read().strip()

def first_unique(n: int) -> int | None:
    for i in range(n, len(data_stream)):
        if len(set(data_stream[i-n: i])) == n:
            return i
        
print(f'puzzle 1: {first_unique(4)}')
print(f'puzzle 2: {first_unique(14)}')