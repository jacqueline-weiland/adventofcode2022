#Open Up File
with open('inputs/day_2_input.txt') as f:
    lines = f.readlines()

#Put into a list
aList = [x.strip().split(" ") for x in lines]

print(aList)

#PART 1

total = 0

for each in aList:
    #check for win or loss
    if each[0] == 'A': #opponent chooses Rock
        if each[1] == 'X': #you choose Rock
            total += 3 #draw
        elif each[1] == 'Y': #you choose Paper
            total += 6 #win --> Paper beats Rock
        elif each[1] == 'Z': #you choose Scissors
            total += 0 #lose --> Scissors loses to Rock
    elif each[0] == 'B': #opponent chooses Paper
        if each[1] == 'X': #you choose Rock
            total += 0 #lose --> Rock loses to Paper
        elif each[1] == 'Y': #you choose Paper
            total += 3 #draw
        elif each[1] == 'Z': #you choose Scissors
            total += 6 #win --> Scissors beats Paper
    elif each[0] == 'C': #opponent chooses Scissors
        if each[1] == 'X': #you choose Rock
            total += 6 #win --> Rock beats Scissors
        elif each[1] == 'Y': #you choose Paper
            total += 0 #lose --> Papers loses to Scissors
        elif each[1] == 'Z': #you choose Scissors
            total += 3 #draw
        
    #give points for choice
    if each[1] == 'X': #you choose Rock
        total += 1
    elif each[1] == 'Y': #you choose Paper
        total += 2
    elif each[1] == 'Z': #you choose Scissors
        total += 3

print(total)    


#PART 2
total = 0

for each in aList:
    #first total addition is for win/lose/draw
    #second total addition is for choice
    if each[0] == 'A': #opponent chooses Rock
        if each[1] == 'X': #you need to lose --> choose Scissors
            total += 0
            total += 3
        elif each[1] == 'Y': #you need to draw --> choose Rock
            total += 3
            total += 1
        elif each[1] == 'Z': #you need to win --> choose Paper
            total += 6
            total += 2
    elif each[0] == 'B': #opponent chooses Paper
        if each[1] == 'X': #you need to lose --> choose Rock
            total += 0
            total += 1
        elif each[1] == 'Y': #you need to draw --> choose Paper
            total += 3
            total += 2
        elif each[1] == 'Z': #you need to win --> choose Scissors
            total += 6
            total += 3
    elif each[0] == 'C': #opponent chooses Scissors
        if each[1] == 'X': #you need to lose --> choose Paper
            total += 0
            total += 2
        elif each[1] == 'Y': #you need to draw --> choose Scissors
            total += 3
            total += 3
        elif each[1] == 'Z': #you need to win --> choose Rock
            total += 6
            total += 1
        
print(total)
