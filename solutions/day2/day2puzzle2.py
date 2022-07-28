with open("./solutions/day2/input.txt", 'r') as inputFile:
    puzzleInput = inputFile.read().splitlines()

totalRibbon = 0

for x in puzzleInput:
    dimensions = x.split("x")
    volume = int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2])
    perimeter1 = (int(dimensions[0]) + int(dimensions[1])) * 2
    perimeter2 = (int(dimensions[1]) + int(dimensions[2])) * 2
    perimeter3 = (int(dimensions[0]) + int(dimensions[2])) * 2
    shortest = min(perimeter1, perimeter2, perimeter3)

    totalRibbon += volume + shortest

print(totalRibbon)
