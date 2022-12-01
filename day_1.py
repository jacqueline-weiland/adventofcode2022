#Open Up File
with open('inputs/day_1_input.txt') as f:
    lines = f.readlines()

#PART 1

aDict = {}
counter = 0
for each in lines:
    if each.strip(): #if the line has a value
        try:
            aDict[counter] += int(each) #it's an additional fruit for an elf so we want to add it to the elf's total
        except: 
            aDict[counter] = int(each) #it's a new elf so we're starting that elf with their calorie count
    else: #if the line is empty
        counter += 1 #move on to next elf
print(aDict)
print(max(aDict.values()))

#PART 2

aList = []
for each in aDict.values():
    aList.append(each)
    
aList = sorted(aList)
print(aList)

print(sum(aList[-3:]))
