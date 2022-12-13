# Format text file into an array of rucksacks
def format_text(text):
    rucksacks = []
    for line in text.splitlines():
        rucksacks.append(line)
    return rucksacks

def find_shared_item(rucksack):
    # Split compartments into tow halves
    half1 = rucksack[0:int((len(rucksack))/2)]
    half2 = rucksack[int((len(rucksack))/2):]
    # Check if a compartment shares an item type 
    for item1 in half1:
        for item2 in half2:
            if item1 == item2:
                return item1
    return

# Calculate item value usng ASCII Values
def item_value(character):
    if ord(character) >= 65 and ord(character) <= 90:
        return (ord(character) - 38)
    else:
        return (ord(character) - 96)

# PART 2 ----
def format_text_as_groups(text):
    groups = []
    group = []
    count = 0
    for line in text.splitlines():
        if count < 3:
            group.append(line)
            count += 1
        else:
            count = 0
            groups.append(group)
            group = []
    return groups

def find_badge(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            print(f"{group[0]}, {group[1]}, {group[2]}")
            print(f"Item match: {item}")
            print(f"Item value: {item_value(item)}")
            return int(item_value(item))
    #return item_value(item)

if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()

    # Functions for part 1
    rucksacks = format_text(f)
    total = 0
    for rucksack in rucksacks:
        shared = find_shared_item(rucksack)
        total += item_value(shared)
    print(total)

    total_badges = 0
    # Part 2
    groups = format_text_as_groups(f)
    for group in groups:
        print(find_badge(group))
        total_badges += find_badge(group)
    print(f"Total: {total_badges}")

