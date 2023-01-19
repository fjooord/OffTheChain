# Object Modeling Example Code

from __future__ import division
import traceback
from ChainChomp import *
from Primatives import *
from Toad import *
from gridBuilder import *
from particleCylinder import *
from Movement import *
import SceneHandling
import globals
# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# call different drawing routines, depending on which number the user types
def handleKeyPressed():

    if (key == 'w'): # Moving chomp forward
        #moveForward()
        if (globals.chompCount > globals.chompCooldown):
            globals.chompMoving = True
        #chompXPos -= (cos(chompRotationY)*rectSize)
        #chompZPos += (sin(chompRotationY)*rectSize)
    elif (key == 'a'): # Turn chomp to the left
        globals.chompRotationY = (globals.chompRotationY + PI/2)%(2*PI)
    elif (key == 's'): # Move chomp backwards
        return
        #chompXPos += (cos(chompRotationY)*rectSize)
        #chompZPos -= (sin(chompRotationY)*rectSize)
    elif (key == 'd'): # Turn chomp to the right
        globals.chompRotationY = (globals.chompRotationY - PI/2)%(2*PI)
    elif (key == '5'):
        SceneHandling.nextScene()
    elif (key == '6'):
        globals.sceneState -= 1
        globals.swappingScene = True
        globals.globals.sceneTimer = 0
    else:
        print 'key not recognized: ', key
    #print(chompXPos)
    

time = 0   # time is used to move objects from one frame to another

def setup():
    size (800, 800, P3D)
    # Initialize all global state variables we will be using in the game
    globals.initialize()
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()
        
    
def draw():
    try:
        # Increment time counter
        globals.time += 0.01
        globals.sceneTimer += 0.01 
        
        # Basic setup
        background (200, 200, 255)  # clear screen and set background to light blue
        # set up the lights
        ambientLight(50, 50, 50);
        lightSpecular(255, 255, 255)
        directionalLight (100, 100, 100, -0.3, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (15.0)
        
        SceneHandling.sceneFTSM(globals.time)
       
    except Exception:
        traceback.print_exc()
        
