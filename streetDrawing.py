import globals 

def drawStreets():
    rectSize = globals.rectSize
    for i in range(len(globals.streetArray)):
        for j in range(len(globals.streetArray[0])):
            if globals.streetArray[i][j] == 0:
                fill(0,255,0)
                drawBox(i, j,rectSize, 10)
            if globals.streetArray[i][j] == 1:
                fill(212,212,212)
                drawSquare(0, i, j,rectSize)
            if globals.streetArray[i][j] == 2:
                fill(255,87,51)
                drawBox(i, j,rectSize, rectSize)
                

                        
def drawSquare(leftRight, i, j, rectSize):
    rectSize = globals.rectSize
    startPoint = 10
    rect(startPoint + (rectSize*j), startPoint+(rectSize*i), rectSize , rectSize)
    
def drawBox(i, j, rectSize, h):
    rectSize = globals.rectSize
    startPoint = 10
    pushMatrix()
    rotateX(PI/2)
    translate((startPoint + (rectSize*(j+0.5))), 0, -(startPoint+(rectSize*(i+0.5))))
    box(rectSize,h,rectSize)
    popMatrix()
