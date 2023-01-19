import globals
from ChainChomp import *
from Primatives import *
from Movement import *
from Toad import *
from streetDrawing import *
from particleCylinder import *

def nextScene():
    globals.sceneState += 1
    globals.swappingScene = True
    globals.sceneTimer = 0
    

def sceneFTSM(time):
    # For ease of refactoring, set all names of variables we use to their global equivalents
    # This is fine since we dont edit the values at all in this file
     
    chompArrLocX = float(globals.chompArrLocX)
    chompArrLocY = float(globals.chompArrLocY)
    chompArrLocXNew = float(globals.chompArrLocXNew)
    chompArrLocYNew = float(globals.chompArrLocYNew)
    chompRotationY = float(globals.chompRotationY)
    chompCooldown = float(globals.chompCooldown)
    chompCount = float(globals.chompCount)
    
    toadArrLocX = float(globals.toadArrLocX)
    toadArrLocY = float(globals.toadArrLocY)
    toadRotationY = float(globals.toadRotationY)
    toadArrLocXNew = float(globals.toadArrLocXNew)
    toadArrLocYNew = float(globals.toadArrLocYNew)
    toadSwapRate = float(globals.toadSwapRate)
    toadCount = float(globals.toadCount)
    
    rectSize = globals.rectSize
 # Start scene FSTM
    
    # Development scene for new characters
    if (globals.sceneState == -1):
        camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
        pushMatrix()
        # Rotate so we are able to view it
        rotateY (-time)

        mySphere(total=64)
        popMatrix()
        
    # Base scene for starting, 
    # Toad taunting the chain chomp
    elif (globals.sceneState == 0):
        if (globals.sceneTimer > 3):
            nextScene()
        camera (0, -100, 300, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
        
        pushMatrix()
        rotateX(PI/2)
        fill(0,255,0)
        rect(-500,-500,1000,1000)
        popMatrix()
        
        # Draw the chain chomp at its global position and rotation
        pushMatrix()
        translate((20*sin(time*4))+20,-40,0)
        #rotateY(-time)
        chainchomp(time, 8)
        popMatrix()
        
        pushMatrix()
        translate(170,-40,0)
        fill(66,40,14)
        rotateX(PI/2)
        scale(10,10,30)
        cylinder(16)
        popMatrix()
        
        pushMatrix()
        translate(-80,-30-(sin(time*10)*10),0)
        fill(66,40,14)
        #rotateX(PI/2)
        #scale(10,10,30)
        drawToad()
        #box(30,30,30)
        popMatrix()
        
        
        
    # Start scene FSTM
    elif (globals.sceneState == 1):
        
        if (globals.sceneTimer > 3):
            nextScene()
        camera (0, -40, 100, 0, -40, 0, 0,  1, 0)  # position of the virtual camera
        sceneTimer = globals.sceneTimer
        pushMatrix()
        rotateX(PI/2)
        fill(0,255,0)
        rect(-500,-500,1000,1000)
        popMatrix()
        
        # Draw the chain chomp at its global position and rotation
        pushMatrix()
        translate(0,-40,0)
        rotateZ(PI/2)
        #scale(10,((sin(time)+1)*10)+10,10)
        scale(10,10,10)
        
        fill(211,211,211)
        # Top half torus
        pushMatrix()
        translate(0,1,0)
        torus(detail_x=6, detail_y=6,half=True)
        popMatrix()
        
        # Bottom half torus
        pushMatrix()
        translate(0,-1,0)
        rotateZ(PI)
        torus(detail_x=6, detail_y=6,half=True)
        popMatrix()
        explosionDirs = globals.explosionDirs
        pushMatrix()
        translate(1,0,0)
        rotateX(PI/2)
        shatterCylinder(sceneTimer, explosionDirs)    
        popMatrix()
        
        
        pushMatrix()
        translate(-1,0,0)
        rotateX(PI/2)
        shatterCylinder(sceneTimer, explosionDirs)
        popMatrix()
    
        popMatrix()
        
    elif (globals.sceneState == 2):
        if (globals.sceneTimer > 8):
            nextScene()
        
        if (globals.sceneTimer < 4):    
            camera (0, -100, 500, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
        else:
        
            # Get the camera position based on the pos and rot of the chomp
            cameraPosX = ((globals.sceneTimer-4)*80) + (cos(chompRotationY)*400)
            cameraPosZ = ((globals.sceneTimer-4)*80) - (sin(chompRotationY)*400)
            
            # Set camera position
            camera (cameraPosX, -150, -cameraPosZ, -((globals.sceneTimer-4.5)*80), 0, 0, 0,  1, 0)  # position of the virtual camera
        
        pushMatrix()
        rotateX(PI/2)
        fill(0,255,0)
        rect(-500,-500,1000,1000)
        popMatrix()
        
        # Draw the chain chomp at its global position and rotation
        pushMatrix()
        if (globals.sceneTimer < 4.5):
            translate(0,-40,0)
        else:
            translate(-((globals.sceneTimer-4.5)*80),-40,0)
        #rotateY(-time)
        chainchomp(globals.sceneTimer, 5)
        popMatrix()
        
        pushMatrix()
        translate(170,-40,0)
        fill(66,40,14)
        rotateX(PI/2)
        scale(10,10,30)
        cylinder(16)
        
        popMatrix()
        
        pushMatrix()
        translate(160,-40,0)
        rotateZ(PI/2)
        scale(5,5,5)
        chainlink()
        popMatrix()
        
        
        pushMatrix()
        if (globals.sceneTimer < 2):
            translate(-80,-20,0)
            pushMatrix()
            fill(255,240,31)
            translate(0,-40,0)
            sphere(5)
            translate(0,-30,0)
            box(10,40,10)
            popMatrix()
            drawToad()
            
        elif(globals.sceneTimer > 2 and globals.sceneTimer < 4):
            #print("hi")
            translate(-80,-20,0)
            #rotateY(PI)
            #print((sceneTimer - 2.0) * PI/2)
            rotateY(-((globals.sceneTimer - 2.0) * PI/2))
            pushMatrix()
            fill(255,240,31)
            translate(0,-40,0)
            sphere(5)
            translate(0,-30,0)
            box(10,40,10)
            popMatrix()
            drawToad(globals.sceneTimer)
            
        else:
            translate(-80-((globals.sceneTimer-4)*80),-20,0)
            rotateY(PI)
            drawToad(globals.sceneTimer)
            
        
        popMatrix()
        
    elif(globals.sceneState == 3):
        # Get the camera position based on the pos and rot of the chomp
    
        moveToad()
        moveForward()
        
        chompLocX = bezierPoint(chompArrLocX, (2*chompArrLocX+chompArrLocXNew)/3,(chompArrLocX+2*chompArrLocXNew)/3,chompArrLocXNew, min(chompCount/chompCooldown,1))
        chompLocZ = bezierPoint(chompArrLocY, (2*chompArrLocY+chompArrLocYNew)/3,(chompArrLocY+2*chompArrLocYNew)/3,chompArrLocYNew, min(chompCount/chompCooldown,1))
        
        
        chompXPos = (chompLocX + 0.5) * rectSize
        chompZPos = (chompLocZ + 0.5) * rectSize
        
        cameraPosX = chompXPos + (cos(chompRotationY)*400)
        cameraPosZ = chompZPos - (sin(chompRotationY)*400)
        
        # Set camera position
        camera (cameraPosX, -400, cameraPosZ, chompXPos, 0, chompZPos, 0,  1, 0)  # position of the virtual camera
        
        # Start scene drawing
        pushMatrix()

        # Draw the chain chomp at its global position and rotation
        pushMatrix()
        chompHeight = bezierPoint(-40,-60,-60, -40, min(chompCount/chompCooldown,1))
        translate(chompXPos,chompHeight,chompZPos)
        rotateY(chompRotationY)
        chainchomp(time,5)
        popMatrix()
        
        # Draw the street layout
        pushMatrix()
        rotateX(PI/2)
        drawStreets()
        popMatrix()
        
        pushMatrix()

        toadLocX = bezierPoint(toadArrLocX, (2*toadArrLocX+toadArrLocXNew)/3,(toadArrLocX+2*toadArrLocXNew)/3,toadArrLocXNew, toadCount/toadSwapRate)+ 0.5
        toadLocY = bezierPoint(toadArrLocY, (2*toadArrLocY+toadArrLocYNew)/3,(toadArrLocY+2*toadArrLocYNew)/3,toadArrLocYNew, toadCount/toadSwapRate)+ 0.5
        
        translate((toadLocX) * rectSize,-20,(toadLocY) * rectSize)
        rotateY(toadRotationY)
        drawToad(time)
        popMatrix()
        
        popMatrix()
    
    elif (globals.sceneState == 6):

        camera (-100, -100, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
        
        pushMatrix()
        rotateX(PI/2)
        fill(0,255,0)
        rect(-500,-500,1000,1000)
        popMatrix()
        
        # Draw the chain chomp at its global position and rotation
        pushMatrix()
        translate(0,-40,0)
        #rotateY(-time)
        chainchomp(PI/2, 8)
        popMatrix()
        
        
        pushMatrix()
        translate(-40,-30,0)
        rotateZ(-PI/2)
        rotateY(-PI/4)
        drawToad(time*4)
        popMatrix()
