# Format text into an array
def format(text):
    arr = []
    for line in text.splitlines(): arr.append(line)
    return arr

# get signal strength
def get_signal_strength(cycle, register):
    return (cycle * register)











if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()

    print(format(f))