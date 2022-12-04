#Reading in file
with open("inputs/day_4_input.txt") as f:
    lines = f.readlines()

#put in a list of lists
aList = [x.strip().split(",") for x in lines]
print(aList)

#PART 1
counter = 0

#list out ranges of each part
for each in aList:
    one_first = int(each[0].split("-")[0])
    one_last = int(each[0].split("-")[1])
    firstList = []
    for i in range(one_first,one_last+1):
        firstList.append(i)
        
    two_first = int(each[1].split("-")[0])
    two_last = int(each[1].split("-")[1])
    secondList = []
    for i in range(two_first,two_last+1):
        secondList.append(i)
        
    #first list entirely contains second list
    if firstList[0] <= secondList[0] and firstList[-1] >= secondList[-1]:
        counter += 1
    #second list entirely contains first list
    elif secondList[0] <= firstList[0] and secondList[-1] >= firstList[-1]:
        counter += 1
    
print(counter)

#PART 2
counter = 0

for each in aList:
    one_first = int(each[0].split("-")[0])
    one_last = int(each[0].split("-")[1])
    firstList = []
    for i in range(one_first,one_last+1):
        firstList.append(i)
        
    two_first = int(each[1].split("-")[0])
    two_last = int(each[1].split("-")[1])
    secondList = []
    for i in range(two_first,two_last+1):
        secondList.append(i)

    if len(set(firstList).intersection(secondList)) > 0:
        counter+=1
print(counter)
