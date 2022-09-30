
"""
Check if string contains a pair of any two letters that appears at least twice in the string without
overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps)
"""
# def check_repeat(entry):



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

with open("C:\\Development\\Python\\adventOfCode\\solutions\\day5\\input.txt", 'r') as inputFile:
    puzzleInput = inputFile.read().splitlines()

for i in puzzleInput:
    if check_split_pair(i):
        nice += 1
    # if check_pairs(i) and check_split_repeat(i):
    #     nice += 1

print(nice)
print(splits)
