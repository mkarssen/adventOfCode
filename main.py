with open("./solutions/day3/input.txt", 'r') as inputFile:
    puzzleInput = inputFile.read()

location = "0,0"

x = 0
y = 0

houses = ([0, 0])

for i in puzzleInput:
    match i:
        case "^":
            y += 1
        case "v":
            y -= 1
        case "<":
            x -= 1
        case ">":
            x += 1

    location = [x, y]
    houses.append(location)

print(houses)
