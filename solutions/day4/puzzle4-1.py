"""
Determine the lowest integer which, when appended to the input string,
corresponds to an MD5 hash that starts with at least 5 zeros.

Steps:
    1. Concatenate input string and current integer (start with 0, increment by 1 each time)
    2. Generate MD5 hash of combined string, decoded into HEX
    3. Count the number of 0s that the hash starts with
    4. If the number of 0s is 5 or more, that is the number you're looking for
"""


import hashlib

from hashlib import md5
init = 'bgvyzdsv'

for i in range(100000000):
    h = md5((init + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        print(i)
        break

# def check_zeros(str_hash):
#     count = 0
#     for i in str_hash:
#         if i == "0":
#             count += 1
#         else:
#             return count


# puzzleInput = "bgvyzdsv"
# extension = 0
# inputString = " "
# outputHash = " "
# zeros = 0
#
# while extension < 5:
#     inputString = puzzleInput + str(extension)
#     outputHash = hashlib.md5(inputString.encode('utf-8')).hexdigest()
#     trimmedString = outputHash[2:(outputHash-2)]
#     zeros = check_zeros(trimmedString)
#     extension += 1
#     print(trimmedString)

# print("Input: " + puzzleInput + str(extension))
# print(hashlib.md5((puzzleInput + str(extension)).encode('utf-8')))