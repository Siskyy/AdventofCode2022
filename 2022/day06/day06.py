def check_if_marker(string):
    for c in string:
        for p in string[string.index(c) + 1:]:
            if c == p:
                return False
    return True

def iterate_signal(signal):
    # Loop through each section of 4 characters
    index = 0
    for n in signal:
        series = signal[index:(index + 4)]
        if check_if_marker(series):
            return (signal.index(series) + 4) # +3 for end or series +1  because array starts a 0
        index += 1
    return False

def iterate_signal_for_message(signal):
    # Loop through each section of 14 characters
    index = 0
    for n in signal:
        series = signal[index:(index + 14)]
        if check_if_marker(series):
            return (signal.index(series) + 14)
        index += 1
    return False


if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()
    # Part 1
    print(iterate_signal(f))
    # Part 2
    print(iterate_signal_for_message(f))