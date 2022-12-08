#Read in file

with open("inputs/day_8_input.txt") as f:
    lines = f.readlines()
#print(lines)

#Put into a list
aList = [x.strip() for x in lines]
print(aList)

#Test Data
#aTestList = ['30373', '25512', '65332', '33549', '35390']
#aList = aTestList

#PART 1
num_rows = len(aList)
num_columns = len(aList[0])

counter = 0
for i in range(len(aList)): #go through each row
    for j in range(len(aList[i])): #go through each tree in each row
        
        #default for each direction is True --> will check to see if proven False
        left_visible = True
        right_visible = True
        up_visible = True
        down_visible = True
        
        #check left
        for m in range(j):
            if aList[i][j] <= aList[i][m]:
                left_visible = False
       #check right
        for n in range(j+1, num_columns):
            if aList[i][j] <= aList[i][n]:
                right_visible = False
       #check up
        for o in range(i):
            if aList[i][j] <= aList[o][j]:
                up_visible = False
        #check down
        for p in range(i+1, num_rows):
            if aList[i][j] <= aList[p][j]:
                down_visible = False
                
        #a long as visible in at least one direction, it's visible
        if left_visible == True or right_visible == True or up_visible == True or down_visible == True:
            counter += 1
print(counter)

#PART 2
num_rows = len(aList)
num_columns = len(aList[0])

highest_score = 0

#print(aList)
for i in range(len(aList)): #go through each row
    for j in range(len(aList[i])): #go through each tree in each row
        
        #set initial values
        left_score = 0
        right_score = 0
        up_score = 0
        down_score = 0    
        
              
        #check left
        for m in range(j):
            if aList[i][j] > aList[i][j-m-1]: #want to start at tree immediately to left
                left_score+=1
            else: #blocked by a tree --> can still see the tree, so add to score, but break loop
                left_score += 1 
                break
       #check right
        for n in range(j+1, num_columns):
            if aList[i][j] > aList[i][n]:
                right_score += 1
            else:
                right_score += 1
                break
       #check up
        for o in range(i):
            if aList[i][j] > aList[i-o-1][j]: #want to start at tree immediately above
                up_score += 1
            else:
                up_score += 1
                break
        #check down
        for p in range(i+1, num_rows):
            if aList[i][j] > aList[p][j]:
                down_score += 1
            else:
                down_score += 1
                break
        
        score = left_score * right_score * up_score * down_score
        
        if score > highest_score:
            highest_score = score

            
print(highest_score)
