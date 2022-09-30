"""
    nice:
        aeiouaeiouaeiou
    naughty:
        jchzalrnumimnmhp
        haegwjzuvuyypxyu
        dvszwmarrgswjxmb
"""


def check_vowels(entry):
    vowels = 0
    for i in entry:
        if i in "aeiou":
            vowels += 1

    if vowels >= 3:
        return True
    else:
        return False


def check_double(entry):
    i = 0
    doubles = 0
    while i < (len(entry)-1):
        if (entry[i] + entry[i+1]) == entry[i] * 2:
            doubles += 1
        i += 1
    if doubles > 0:
        return True
    else:
        return False


def check_sequence(entry):
    if ("ab" in entry) or ("bc" in entry) or ("pq" in entry) or ("xy" in entry):
        return False
    else:
        return True


nice = 0

with open("C:/Development/Python/adventOfCode/solutions/day5/input.txt", 'r') as inputFile:
    puzzleInput = inputFile.read().splitlines()

for i in puzzleInput:
    if check_double(i) and check_sequence(i) and check_vowels(i):
        nice += 1

print(nice)
