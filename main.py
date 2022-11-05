import re


"""
Check if string contains a pair of any two letters that appears at least twice in the string without
overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps)
"""
def check_repeat(entry):
    i = 0
    while i < (len(entry) - 3):
        if (entry[i:i+1] in entry[i+2:]):
            repeats = True
        i += 1
    print(entry)
    print(repeats)


"""
It contains at least one letter which repeats with exactly one letter between them,
like xyx, abcdefeghi (efe), or even aaa.
"""
def check_split_pair(entry):
    i = 0
    split_pair = 0
    while i < (len(entry) - 3):
        if entry[i] == entry[i + 2]:
            split_pair += 1
            splits.append(entry[i:i+3])
        i += 1

    if split_pair > 0:
        return True
    else:
        return False


nice = 0
splits = []

with open("C:\Development\Python\\adventOfCode\solutions\day5\day5input.txt", 'r') as inputFile:
    puzzleInput = inputFile.read().splitlines()

for i in puzzleInput:
    check_repeat(i)
    # if check_split_pair(i):
    #     nice += 1
    # if check_pairs(i) and check_split_repeat(i):
    #     nice += 1

print(nice)

