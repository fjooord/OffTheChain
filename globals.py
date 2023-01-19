# streetArray = []
# chompXPos, chompZPos, chompRotationY, chompTurning, turnCount, rectSize = 0,0,0,0,0,0
# chompArrLocX, chompArrLocY = 0,0
# chompArrLocXNew, chompArrLocYNew = 0,0 
# chompCount, chompMoving, chompCooldown = 0,0,0
# toadArrLocX, toadArrLocY, toadRotationY = 0,0,0
# toadArrLocXNew, toadArrLocYNew, toadRotationYNew = 0,0,0
# toadCount,toadSwapRate = 0,0
# sceneState = 5
# swappingScene = True
# sceneTimer = 0
# explosionDirs = []
from gridBuilder import *
from particleCylinder import *
def initialize():
    
    global streetArray
    global chompXPos, chompZPos, chompRotationY, chompTurning, turnCount, rectSize
    global chompArrLocX, chompArrLocY
    global chompArrLocXNew, chompArrLocYNew
    global chompCount, chompMoving, chompCooldown
    global toadArrLocX, toadArrLocY, toadRotationY
    global toadArrLocXNew, toadArrLocYNew, toadRotationYNew
    global toadArrLocXNew2, toadArrLocYNew2, toadRotationYNew2
    global toadCount,toadSwapRate
    # Create Array that will be placeholder for the streets
    
    
    # Create variable to create a FSTM for the different scenes
    global time, sceneState, swappingScene, sceneTimer
    time = 0
    sceneState = 0
    swappingScene = True
    sceneTimer = 0
    
    global explosionDirs
    
    explosionDirs = makeDirections()
    
    streetArray = makeStreetGrid()
    
    
    chompArrLocX = 1
    chompArrLocY = 1
    
    
    chompArrLocXNew = 1
    chompArrLocYNew = 1
    
    
    chompCount  = 0
    chompMoving = False
    chompCooldown = 20
    
    
    toadArrLocX = 1
    toadArrLocY = 3
    toadRotationY = -PI/2
    
    
    # Random movement in grid, in available directions
    
    toadArrLocXNew = 1
    toadArrLocYNew = 3
    
    toadArrLocXNew2 = 1
    toadArrLocYNew2 = 4
    
    toadCount = 61
    
    toadSwapRate = 45
    rectSize=100
    
    chompXPos = (chompArrLocX  + 0.5) * rectSize
    chompZPos = (chompArrLocY + 0.5) * rectSize
    chompRotationY = PI/2
    
    chompTurning = False
    turnCount = 0
    
