import numpy as np
def find_top_three(file) -> NDArray:
    total = 0
    top_three = np.array([0, 0, 0])
    for line in file:
        try:
            total += int(line)
        except:
            if total > np.min(top_three): 
                top_three[np.argmin(top_three)] = total
            total = 0
    return top_three
        
file_name = 'input.txt'
with open(file_name) as input_file:
    top_three = find_top_three(input_file)
    print(f'puzzle 1: {max(top_three)}')
    print(f'puzzle 2: {sum(top_three)}')