# Format text into an array
def format(text):
    arr = []
    for line in text.splitlines(): arr.append(line)
    return arr

# get signal strength
def get_signal_strength(cycle, register):
    return (cycle * register)

# Main function which iterates though each of the cycles, adding to the signal register value and keeping count of the cycle
def main(program):
    # Set the cycle to 0 and X to 1
    cycles, X = 1, 1
    # Signal strength total for 20th, 60th, 100th ... cycle
    signal_strength_total = 0
    # List containing desired cycles
    desired_cycles = [20, 60, 100, 140, 180, 220]
    # For every line in the program
    for instruction in program:
        # If the instruction is a noop value, add 1 to the cycle count
        if instruction == 'noop':
            # Do nothing and complete one cycle
            cycles += 1
        else:
            # This process take 2 cycles to complete so increase cycles by 1 first
            cycles += 1
            # Then check if this is a desired cycle
            if cycles in desired_cycles:
                signal_strength_total += get_signal_strength(cycles, X)
            # Add second second cycle
            cycles += 1
            # Add the value to the register
            X += int(instruction[5:])
            
        if cycles in desired_cycles:
            signal_strength_total += get_signal_strength(cycles, X)

    return signal_strength_total

# PART 2 - Using the sprite --------------------------------------------

# Create a grid which is 40 wide and 6 high
def blank_grid():
    grid = []
    for n in range(0, 240): grid.append("#")
    return grid

# Displays the grid in a 40x6 format
def display_grid(grid):
    index = 0
    # For every row (6 rows)
    for row in range(0, 6):
        # For every position in that row (40 positions)
        for col in range(0, 40):
            print(grid[index], end="")
            index += 1
        print('\n', end="")
    return


def check_if_touching(pixel, sprite):
    # If the sprite is on same spot as current pixel
    if (sprite - 1 <= pixel <= sprite + 1):
        return True
    return False

def draw(program):
    # Start with an empty canvas
    canvas = blank_grid()
    # Set the cycle to 0 and X to 1
    cycles = 1
    # Sets the current pixel to draw on
    pixel = 0
    # Sprite Position will be '###.....................................'
    sprite_pos = 1
    # For every line in the program
    for instruction in program:
        # Check if pixel is at the end of a row
        if (pixel % 40 == 0) and (pixel != 0):
            # Set pixel to 0 again (but on the next row)
            pixel = 0
        # If the instruction is a noop value
        if instruction == 'noop':
            # Check if the sprite is not touching a pixel
            if not check_if_touching(pixel, sprite_pos):
                # if the sprite is NOT touching the pixel -> change that pixel to a '.'
                canvas[cycles - 1] = ' '
            # Complete one cycle and move to next pixel
            cycles += 1
            pixel += 1

        # If the line is an 'addx V', go through 2 cycles before moving the sprite
        else:
            # First Cycle starts -> sprite stays in same position
            # Check if the sprite is not touching a pixel 
            if not check_if_touching(pixel, sprite_pos):
                # if the sprite is NOT touching the pixel -> change that pixel to a '.'
                canvas[cycles - 1] = ' '
            
            # First cycle Complete + move to next pixel/cycle
            cycles += 1
            pixel += 1
            # Need to check again during (this is a 2 cycle process)
            if (pixel % 40 == 0) and (pixel != 0):
                pixel = 0
            if not check_if_touching(pixel, sprite_pos):
                canvas[cycles - 1] = ' '
            # Second cycle Complete + move to next pixel/pixel
            cycles += 1
            pixel += 1
            # Move the sprite
            sprite_pos += int(instruction[5:])
    return canvas


if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()

    # PART 2
    ans = draw(format(f))
    display_grid(ans)