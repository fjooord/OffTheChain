import globals

def moveToad():
    # Random movement in grid, in available directions

    globals.toadCount +=1
    if (globals.toadCount > globals.toadSwapRate):
        globals.toadCount = 0
        globals.toadArrLocX = globals.toadArrLocXNew
        globals.toadArrLocY = globals.toadArrLocYNew
        
        
        chompArrLocX = globals.chompArrLocX 
        chompArrLocY = globals.chompArrLocY
        chompRotationY = globals.chompRotationY
        toadArrLocX = globals.toadArrLocX
        toadArrLocY = globals.toadArrLocY
        
        # Make array for cases
        cases = []
        # Squared distance to chomp
        chompDist = (((chompArrLocY) - (toadArrLocY))**2 + ((chompArrLocX) - (toadArrLocX))**2) 
        
        # check which squares are available and append its case if so
        if (globals.streetArray[toadArrLocY+1][toadArrLocX] == 1):
            # If this distance is farther away from chomp then it can go here
            if ((((chompArrLocY) - (toadArrLocY+1))**2 + ((chompArrLocX) - (toadArrLocX))**2) > chompDist): 
                cases.append(0)
        if (globals.streetArray[toadArrLocY][toadArrLocX+1] == 1):
            if ((((chompArrLocY) - (toadArrLocY))**2 + ((chompArrLocX) - (toadArrLocX+1))**2) > chompDist): 
                cases.append(1)
        if (globals.streetArray[toadArrLocY-1][toadArrLocX] == 1):
            if ((((chompArrLocY) - (toadArrLocY-1))**2 + ((chompArrLocX) - (toadArrLocX))**2) > chompDist): 
                cases.append(2)
        if (globals.streetArray[toadArrLocY][toadArrLocX-1] == 1):
            if ((((chompArrLocY) - (toadArrLocY))**2 + ((chompArrLocX) - (toadArrLocX-1))**2) > chompDist): 
                cases.append(3)
        
        # return if no better position for the toad
        if (len(cases) == 0):
            return
        
        # Choose random available direction
        nextCase = cases[int(random(len(cases)))]
        #print(len(cases))
        # Assign proper value
        if (nextCase == 0):
            globals.toadArrLocYNew = toadArrLocY + 1
            globals.toadRotationY = -PI/2
        elif (nextCase == 1):
            globals.toadArrLocXNew = toadArrLocX + 1
            globals.toadRotationY = 0
        elif (nextCase == 2):
            globals.toadArrLocYNew = toadArrLocY - 1
            globals.toadRotationY = PI/2
        elif (nextCase == 3):
            globals.toadArrLocXNew = toadArrLocX - 1
            globals.toadRotationY = PI
        
        


def moveForward():

    globals.chompCount += 1
    if (globals.chompMoving):
        globals.chompArrLocX = globals.chompArrLocXNew 
        globals.chompArrLocY = globals.chompArrLocYNew 
        globals.chompCount = 0
        globals.chompMoving = False
        
        chompArrLocX = globals.chompArrLocX 
        chompArrLocY = globals.chompArrLocY
        chompArrLocXNew = globals.chompArrLocXNew
        chompArrLocYNew = globals.chompArrLocYNew
        chompRotationY = globals.chompRotationY
        toadArrLocX = globals.toadArrLocX
        toadArrLocY = globals.toadArrLocY
        toadArrLocXNew = globals.toadArrLocXNew
        toadArrLocYNew = globals.toadArrLocYNew
        
        if (abs(chompRotationY) == PI/2):
            if (globals.streetArray[chompArrLocY+1][chompArrLocX] == 1):
                # If moving into toad square you win!
                if (toadArrLocX == chompArrLocX and toadArrLocY == chompArrLocY+1):
                    globals.sceneState = 6
                else:   
                    globals.chompArrLocYNew = chompArrLocY + 1
                    
        elif (abs(chompRotationY) == PI):
            if (globals.streetArray[chompArrLocY][chompArrLocX+1] == 1):
                if (toadArrLocX == chompArrLocX+1 and toadArrLocY == chompArrLocY):
                    globals.sceneState = 6
                else: 
                    globals.chompArrLocXNew = chompArrLocX + 1
                    
        elif (abs(chompRotationY) == 3*PI/2):
            if (globals.streetArray[chompArrLocY-1][chompArrLocX] == 1):
                if (toadArrLocX == chompArrLocX and toadArrLocY == chompArrLocY-1):
                    globals.sceneState = 6
                else: 
                    globals.chompArrLocYNew = chompArrLocY - 1
      
        elif (chompRotationY == 0 or abs(chompRotationY) == 2*PI):
            if (globals.streetArray[chompArrLocY][chompArrLocX-1] == 1):
                if (toadArrLocX == chompArrLocX-1 and toadArrLocY == chompArrLocY):
                    globals.sceneState = 6
                else: 
                    globals.chompArrLocXNew = chompArrLocX - 1
                
