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

    print(f"Number of cycles: {cycles}")
    print(f"Register Value: {X}")
    print(f"Total Signal Strength: {signal_strength_total}")
    return


    return




if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()

    main(format(f))