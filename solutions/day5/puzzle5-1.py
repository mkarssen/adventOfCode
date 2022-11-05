"""
    nice:
        aeiouaeiouaeiou
    naughty:
        jchzalrnumimnmhp
        haegwjzuvuyypxyu
        dvszwmarrgswjxmb
"""

import sqlite3 as sql

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


niceID = 1
naughtyID = 1
niceCount = 0
nice = []
naughty = []

# Create temporary database in memory
db = sql.connect(":memory:")
print("Database created in RAM")

# Create table of recipients with attributes for each Nice/Naughty criterion
db.execute('''CREATE TABLE NICE
    (ID INT PRIMARY KEY NOT NULL,
    RECIP TEXT NOT NULL,
    VOWELS TEXT NOT NULL,
    DOUBLE TEXT NOT NULL,
    SEQUENCE TEXT NOT NULL);''')
print("SQL Table Created: NICE")

db.execute('''CREATE TABLE NAUGHTY
    (ID INT PRIMARY KEY NOT NULL,
    RECIP TEXT NOT NULL,
    VOWELS TEXT NOT NULL,
    DOUBLE TEXT NOT NULL,
    SEQUENCE TEXT NOT NULL);''')
print("SQL Table Created: NAUGHTY")

# Open input file and split the lines into a list
with open("C:\Development\Python\\adventOfCode\solutions\day5\day5input.txt", 'r') as inputFile:
    puzzleInput = inputFile.read().splitlines()


for i in puzzleInput:
    double = check_double(i)
    sequence = check_sequence(i)
    vowels = check_vowels(i)
    if double and sequence and vowels:
        db.execute("INSERT INTO NICE(ID,RECIP,VOWELS,DOUBLE,SEQUENCE) VALUES (?, ?, ?, ?, ?)",
                   (niceID, str(i), str(double), str(sequence), str(vowels)))
        niceID += 1
        niceCount += 1
        nice.append(i)
    else:
        db.execute("INSERT INTO NAUGHTY(ID,RECIP,VOWELS,DOUBLE,SEQUENCE) VALUES (?, ?, ?, ?, ?)",
                   (naughtyID, str(i), str(double), str(sequence), str(vowels)))
        naughtyID += 1
        naughty.append(i)

cursor = db.execute('''SELECT ID, RECIP, VOWELS, DOUBLE, SEQUENCE FROM NICE''')


for row in cursor:
    print("ID: ", row[0])
    print("Recipient: ", row[1])
    print("Vowel Test Passed: ", row[2])
    print("Double Test Passed: ", row[3])
    print("Sequence Test Passed: ", row[4])


print(niceCount)

db.close()
