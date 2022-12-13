def format_text(text):
    rota = []
    elf_pair = []
    for line in text.splitlines():
        elf_pair = line.split(',')
        rota.append(elf_pair)
    return rota

# Find the assignments that overlap
def find_full_overlaps(rota):

    full_overlaps = 0
    for pair in rota:
        elf_1_first = int(pair[0][0:pair[0].index("-")])
        elf_1_last = int(pair[0][(pair[0].index("-") + 1):])
        elf_2_first = int(pair[1][0:pair[1].index("-")])
        elf_2_last = int(pair[1][(pair[1].index("-") + 1):])
        
        # Check if there is a full overlap
        if ((elf_1_first <= elf_2_first) and (elf_1_last >= elf_2_last)) or ((elf_1_first >= elf_2_first) and (elf_1_last <= elf_2_last)):
            full_overlaps += 1
    return full_overlaps


# part 2 ----

def find_overlaps(rota):

    overlaps = 0
    for pair in rota:
        elf_1_first = int(pair[0][0:pair[0].index("-")])
        elf_1_last = int(pair[0][(pair[0].index("-") + 1):])
        elf_2_first = int(pair[1][0:pair[1].index("-")])
        elf_2_last = int(pair[1][(pair[1].index("-") + 1):])

        # Check if there is a full overlap
        if ((elf_1_first <= elf_2_first) and (elf_1_last >= elf_2_first)):
            overlaps += 1
        elif ((elf_1_first >= elf_2_first) and (elf_1_first <= elf_2_last)):
            overlaps += 1
    return overlaps



if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()
    
    rota = format_text(f)
    print(f"Total full overlaps: {find_full_overlaps(rota)}")

    # part 2 ---
    print(f"Total overlaps: {find_overlaps(rota)}")