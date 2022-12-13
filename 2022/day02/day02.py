# --- Day 2: Rock Paper Scissors ---

# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

# Assuming X,Y,Z = Rock, Paper, Scissors
scoring = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
elf_stats = [0, 0, 0]
you_stats = [0, 0, 0]


def format_txt(text):
    rounds = []
    for line in guide.splitlines():
        game = line.split()
        rounds.append(game)
    return rounds

def play(elf, you):
    if scoring[elf] == scoring[you]:
        result = ["draw", (scoring[elf] + 3), (scoring[you] + 3)]
    elif (elf == "A" and you == "Y") or (elf == "B" and you == "Z") or (elf == "C" and you == "X"):
        result = ["you", scoring[elf], (scoring[you] + 6)]
    elif (elf == "A" and you == "Z") or (elf == "B" and you == "X") or (elf == "C" and you == "Y"):
        result = ["elf", (scoring[elf] + 6), scoring[you]]
    return result
    
def count_score(rounds):
    elf_score = {"score": 0, "wins": 0, "losses": 0}
    you_score = { "score": 0, "wins": 0, "losses": 0}
    for game in rounds:
        result = play(game[0], game[1])
        # Just for stats:
        record_stats(game)
        elf_score["score"] = elf_score["score"] + result[1]
        you_score["score"] = you_score["score"] + result[2]
    print("You Win!") if you_score["score"] > elf_score["score"] else print("You Lose!")
    return [elf_score, you_score, len(rounds)]

# two functions just for stats
def record_stats(game):
    if game[0] == "A": elf_stats[0] += 1
    if game[0] == "B": elf_stats[1] += 1
    if game[0] == "C": elf_stats[2] += 1
    if game[1] == "X": you_stats[0] += 1
    if game[1] == "Y": you_stats[1] += 1
    if game[1] == "Z": you_stats[2] += 1
    return

def calc_percent(elf, you):

    total = sum(you)
    rocks = round(you[0] / total * 100, 1)
    papers = round(you[1] / total * 100, 1)
    scissors = round(you[2] / total * 100, 1)
    return [rocks, papers, scissors] 


# part 2
# X = lose, Y = Draw, Z = Win

def play2(elf, you):
    if you == "Y":
        result = ["draw", (scoring[elf] + 3), (scoring[elf] + 3)]
    elif you == "X":
        if elf == "A":
            result = ["elf", scoring[elf] + 6, (scoring["C"])]
        elif elf == "B":
            result = ["elf", scoring[elf] + 6, (scoring["A"])]
        elif elf == "C":
            result = ["elf", scoring[elf] + 6, (scoring["B"])]
    elif you == "Z":
        if elf == "A":
            result = ["elf", scoring[elf], (scoring["B"] + 6)]
        elif elf == "B":
            result = ["elf", scoring[elf], (scoring["C"] + 6)]
        elif elf == "C":
            result = ["elf", scoring[elf], (scoring["A"] + 6)]
    return result

def count_score2(rounds):
    elf_score = {"score": 0, "wins": 0, "losses": 0}
    you_score = { "score": 0, "wins": 0, "losses": 0}
    for game in rounds:
        result = play2(game[0], game[1])
        # Just for stats:
        record_stats(game)
        elf_score["score"] = elf_score["score"] + result[1]
        you_score["score"] = you_score["score"] + result[2]
    print("You Win!") if you_score["score"] > elf_score["score"] else print("You Lose!")
    return [elf_score, you_score, len(rounds)]

if __name__ == '__main__':
    
    with open('test.txt') as inputs:
        guide = inputs.read()

    total = count_score(format_txt(guide))
    total2 = count_score2(format_txt(guide))
    print("Elf:", total2[0]["score"])
    print("You:", total2[1]["score"])

    # Stats (uncomment if not wanted)
    print(f"Games played: {total2[2]}")
    stats = calc_percent(elf_stats, you_stats)
    print(f"Rock: {stats[0]}%, Paper: {stats[1]}%, Scissors: {stats[2]}%")