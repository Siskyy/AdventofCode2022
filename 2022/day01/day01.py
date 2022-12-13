import sys
# USAGE: python3 day01.py <test.txt> [can input any test file]
with open(sys.argv[1], 'r') as test_data:
    input = test_data.read()

# format data into an array
def format_data(input):
    arr = []
    for line in input.splitlines():
        arr.append(line)
    return arr

def elf_count(data):
    largest = {"elf": 1, "calories": 0}
    current_elf = 1
    current_calories = 0
    elf_data = {}
    for food in data:
        if not food.isdigit():
            if elf_data[current_elf] > largest["calories"]:
                largest["elf"] = current_elf
                largest["calories"] = elf_data[current_elf]
            current_elf += 1
            current_calories = 0
            continue
        else:
            current_calories += int(food)
            elf_data.update({current_elf: current_calories})
    return [elf_data, largest]

data = format_data(input)


answer = elf_count(data)
print(answer[1])



# Part 2

def get_top_three(elves):
    print(elves)
    arr = []
    for elf in elves:
        arr.append(elves[elf])
    
    arr.sort()
    total_top_three = sum(arr[-3:])
    return total_top_three

print(get_top_three(answer[0]))
