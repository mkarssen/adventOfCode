with open("./solutions/day2/day5input.txt", 'r') as inputFile:
    puzzleInput = inputFile.read().splitlines()

totalPaperNeeded = 0

for x in puzzleInput:
    dimensions = x.split("x")
    side1 = int(dimensions[0]) * int(dimensions[1])
    side2 = int(dimensions[1]) * int(dimensions[2])
    side3 = int(dimensions[0]) * int(dimensions[2])
    smallestSide = min(side1, side2, side3)
    totalPaperNeeded += 2 * side1 + 2 * side2 + 2 * side3 + smallestSide

print(totalPaperNeeded)

