#Reading in File

with open('inputs/day_3_input.txt') as f:
    lines = f.readlines()
#print(lines)

#PART 1

#Put into a list with 2 parts    
splitList = [(x[:len(x)//2], x[len(x)//2:].strip()) for x in lines]
#print(splitList)

#find common letter between each part of each rucksack
letterList = []
for each in splitList:
    letterList.append(''.join(set(each[0]).intersection(each[1])))
print(letterList)

runningTotal = 0
#find value of each common letter
for each in letterList:
    if each.isupper() == True:
        runningTotal += ord(each)-38 #A starts at 65 and we want it to start at 27
    elif each.islower() == True:
        runningTotal += ord(each)-96 #a starts at 97 and we want it to start at 1
print(runningTotal)

#PART 2

#get rid of newline characters (couldn't figure out how to include it in list comprehension)
newlines = []
for each in lines:
    newlines.append(each.strip())

#putting inputs in groups of three
aList = [newlines[i * 3:(i + 1) * 3] for i in range((len(newlines) + 3 - 1) // 3 )]

#find common letter between each of the group of threes
letterList = []
for each in aList:
    letterList.append(''.join(set(each[0]).intersection(each[1]).intersection(each[2])))
print(letterList)

runningTotal = 0
#find value of each common letter
for each in letterList:
    if each.isupper() == True:
        runningTotal += ord(each)-38 #A starts at 65 and we want it to start at 27
    elif each.islower() == True:
        runningTotal += ord(each)-96 #a starts at 97 and we want it to start at 1
print(runningTotal)
