priority = lambda c: ord(c) - ord('a') + 1 if ord(c) >= ord('a') else ord(c) - ord('A') + 27

def puzzle1(rucksacks):
    sizes = [len(rucksack)//2 for rucksack in rucksacks]
    priorities = [priority( (set(rucksack[:size]) & set(rucksack[size:])).pop() ) 
                  for size, rucksack in zip(sizes, rucksacks)]
    return sum(priorities)  


def puzzle2(rucksacks):
    priorities = [priority( (set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])).pop() ) 
                  for i in range(0, len(rucksacks), 3)]
    return sum(priorities)    
        
        
file_name = 'Day03/input.txt'
with open(file_name) as input_file:
    rucksacks = [line.strip() for line in input_file]#.readlines()

print(f'puzzle 1: {puzzle1(rucksacks)}')
print(f'puzzle 2: {puzzle2(rucksacks)}')