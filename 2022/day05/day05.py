
def get_stacks(text):
    cut = text.split('\n\n')
    return cut[0]

def operations(text):
    cut = text.split('\n\n')
    operations = []
    for line in cut[1].splitlines():
        operations.append(line)
    return operations

# Put each stack into an array
# So 9 arrays of crates

def stacks_arrays(text):
    crates, one_stack = [], []

    row = 0
    count = 0
    # 9 different stacks
    for stack in range(0,9):
        # Each stack has a maxmimum height of 8 crates
        for crate in range(0,8):
            one_stack.append(text[row:(row+3)])
            # change row to position under current crate (a row is 36 chars)
            row += 36
        # Once the full stack of crates has been added to one_stack -> add it to the array of stacks
        crates.append(one_stack)
        # Clear the stack
        one_stack = []
        # Move right to next stack '[A] ' is 4 spaces
        count += 4
        row = 0 + count
    return crates


def move(before, after):

    # get the height of the stacks
    height_before = 0
    for space in crates[before]:
        if space != "   ":
            height_before += 1

    height_after = 0
    for space in crates[after]:
        if space != "   ":
            height_after += 1
            
    # If a stack has a height of 8, add a space above so that a crate can be placed on top
    if height_before == len(crates[before]):
        crates[before].insert(0, '   ')
    if height_after == len(crates[after]):
        crates[after].insert(0, '   ')

    # now take the top block from before and then add it to the after stack
    
    # get top letter of the stacks
    top_letter = crates[before][- height_before]
    top_letter_after = crates[after][- height_after]

    # print(f"Stack {(before + 1)}: {crates[before]}, Height: {height_before}, Top crate: {top_letter}")
    # print(f"Stack {(after + 1)}: {crates[after]}, Height: {height_after}, Top crate: {top_letter_after}")

    # The crane picks up the crate on the top of the pile
    holding = crates[before][(crates[before].index(top_letter))]
    # Once crate is picked up, remove it from the stack
    crates[before][(crates[before].index(top_letter))] = '   '
    # Place the crate onto the after stack
    crates[after][(crates[after].index(top_letter_after)) - 1] = holding
    return

def operate(operation):
    
    split = operation.split(' from ') # splits move "11 from 8 to 3" into ["move 11", "8 to 3"]
    number_of_moves = int((split[0].split(" "))[1])
    location = split[1].split(" to ")
    # Call the move function <number_of_moves> times
    for action in range(0,number_of_moves):
        move(int(location[0]) - 1, int(location[1]) - 1)
    return

# Part 2 - CrateMover9001 --------------------------------------------------------
# Crate can now pick up multiple crates at once

def get_height(before, after):
    height_before = 0
    for space in crates[before]:
        if space != "   ":
            height_before += 1
    height_after = 0
    for space in crates[after]:
        if space != "   ":
            height_after += 1
    return [height_before, height_after]

def operate_9001(operation):

    split = operation.split(' from ') # splits move "11 from 8 to 3" into ["move 11", "8 to 3"]
    number_of_moves = int((split[0].split(" "))[1])
    location = split[1].split(" to ")
    before, after = int(location[0]) - 1, int(location[1]) - 1

    heights = get_height(before, after)

    # Add enough space on top of after stack so that crates can be placed
    space_needed = number_of_moves - crates[after].count('   ')
    while crates[after].count('   ') <= number_of_moves:
        crates[after].insert(0, '   ')
    
    # get top letter of the stacks
    top_letter = crates[before][- heights[0]]
    top_letter_after = crates[after][- heights[1]]
    # Crate picks up top <number of crates> crates from the before stack
    holding = crates[before][(crates[before].index(top_letter)):((crates[before].index(top_letter)) + number_of_moves)] # e.g. ['[S]', '[G]', '[P]']
    
    # Replace the picked up crates with an empty space
    for slot in crates[before][(crates[before].index(top_letter)):((crates[before].index(top_letter)) + number_of_moves)]:
        crates[before][crates[before].index(slot)] = '   '
    # Place the crate onto the after stack
    index = len(holding) - 1
    for crate in holding:
        crates[after][(crates[after].index(top_letter_after)) - 1] = holding[index]
        top_letter_after = holding[index]
        index -= 1
    # Remove unessary excess space from stacks
    while crates[before].count('   ') > 8:
        crates[before].pop(0)
    return


if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()

    operations = operations(f)
    
    crates = stacks_arrays(get_stacks(f))
    for operation in operations:
        operate_9001(operation)
    
    # Print the top crates for each row
    for stack in crates:
        height = 0
        top_crates = ""
        for position in stack:
            if position != "   ":
                height += 1
        print(stack[-height].strip('[]'))
