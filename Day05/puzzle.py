import re

def read_stacks(lines):
    n = len(lines[0].split())
    stacks = [[] for i in range(n)]
    for line in lines[1:]:
        for i, cargo in zip(range(n), (line + 4 * n * ' ')[1::4]): # lines are padded with enough space 
            if cargo != ' ':
                stacks[i].append(cargo)
    return stacks            

def read_moves(lines) -> list[list[int]]:
    return [list(map(int, re.findall(r'\d+', line))) for line in lines]

def execute_moves_900(stacks, moves): 
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]-1].append(stacks[move[1]-1].pop())    
    return stacks

def execute_moves_901(stacks, moves):
    for move in moves:
        stacks[move[2]-1] += stacks[move[1]-1][-move[0]:]
        stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]
    return stacks

file_name = 'Day05/input.txt'
with open(file_name) as input_file:
    stack_text, move_text = input_file.read().split('\n\n')

stacks = read_stacks(stack_text.split('\n')[::-1])
moves = read_moves(move_text.split('\n'))
after_900 = execute_moves_900([stack.copy() for stack in stacks], moves)
after_901 = execute_moves_901([stack.copy() for stack in stacks], moves)

print(f'puzzle 1: {"".join([stack[-1] for stack in after_900])}')
print(f'puzzle 2: {"".join([stack[-1] for stack in after_901])}')