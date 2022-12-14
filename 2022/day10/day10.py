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

# PART 2 - Using the sprite

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
    # Set row_number to 0 (starting row)
    row_number = 0
    position = 0
    # For every line in the program
    for instruction in program:
        # print(display_grid(canvas))
        # If the instruction is a noop value
        if instruction == 'noop':
            print("NOOP")
            print(f"Sprite: [{sprite_pos-1},{sprite_pos},{sprite_pos+1}], Pixel: [{pixel}]")
            print(f"Sprite is touching Pixel") if check_if_touching(pixel, sprite_pos) else print("Sprite is NOT touching Pixel") 

            # Check if the sprite is not touching a pixel
            if not check_if_touching(pixel, sprite_pos):
                # if the sprite is NOT touching the pixel -> change that pixel to a '.'
                canvas[cycles - 1] = ' '

            # Check if pixel is at the end of a row
            if (pixel % 40 == 0) and (pixel != 0):
                row_number += 1
                # Set pixel to 0 again (but on the next row)
                pixel = 0
                # Continue cycles
                cycles += 1
            else:
                # Complete one cycle and move to next pixel
                cycles += 1
                pixel += 1
            print(display_grid(canvas))
        # If the line is an 'addx V', go through 2 cycles before moving the sprite
        else:
            print(f"ORDER: {instruction}")
            print(f"Sprite: [{sprite_pos-1},{sprite_pos},{sprite_pos+1}], Pixel: [{pixel}]")
            print(f"Sprite is touching Pixel") if check_if_touching(pixel, sprite_pos) else print("Sprite is NOT touching Pixel") 
            
            # First Cycle starts -> sprite stays in same position
            # Check if the sprite is not touching a pixel 
            if not check_if_touching(pixel, sprite_pos):
                # if the sprite is NOT touching the pixel -> change that pixel to a '.'
                canvas[cycles - 1] = ' '
            
            # Check if pixel is at the end of a row
            if (pixel % 40 == 0) and (pixel != 0):
                row_number += 1
                pixel = 0
                cycles += 1
            else:
                # One cycle Complete + move to next pixel
                cycles += 1
                pixel += 1

            print(display_grid(canvas))
            print(f"Sprite: [{sprite_pos-1},{sprite_pos},{sprite_pos+1}], Pixel: [{pixel}]")
            print(f"Sprite is touching Pixel") if check_if_touching(pixel, sprite_pos) else print("Sprite is NOT touching Pixel") 

            if not check_if_touching(pixel, sprite_pos):
                canvas[cycles - 1] = ' '

            
            # Check if pixel is at the end of a row
            if (pixel % 40 == 0) and (pixel != 0):
                row_number += 1
                pixel = 0
                cycles + 1
            else:
                # One cycle Complete + move to next pixel
                cycles += 1
                pixel += 1

            print(display_grid(canvas))
            # Add the value to the register
            print(f"Sprite moving {instruction[5:]}")

            sprite_pos += int(instruction[5:])
            
    return canvas


if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()

    #print(main(format(f)))
    ans = draw(format(f))
    # print(ans)
    # Create blank canvas
    
    display_grid(ans)