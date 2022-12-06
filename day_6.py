#Read text file
with open("inputs/day_6_input.txt") as f:
    input = f.read()
print(input)

#PART 1
for i in range(len(input)):
    letters = input[i:i+4]
    if len(set(letters)) == 4:
        print(i+4) #adding 4 because i starts at 0 and then we must go to end of string
        break

#PART 2
for i in range(len(input)):
    letters = input[i:i+14]
    if len(set(letters)) == 14:
        print(i+14) #adding 14 because i starts at 0 and then we must go to end of string
        break
