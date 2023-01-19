from Primatives import *

def chainchomp(t, linkNum):
    # Draw main black body
    ## Draw top shell
    drawBody(t)
    # Draw chain
    fill (255, 0, 0)
    pushMatrix()
    #translate (-30, 0, 0)
    rotateZ(PI/2)
    translate(0,-45,0)
    #box(20)
    scale(5,5,5)
    chain(linkNum)
    popMatrix()

def drawBody(t):
    topClamShell(t)
    bottomClamShell(t)
    
def topClamShell(time):
    pushMatrix()
    rotateX(PI/2)
    rotateY(((sin(time*15) + 1) * PI/8)+PI/8)
    #rotateY(PI/4)
    mySphere()
    mySphere(38, 160, 0, 32,6)
    drawEyes()
    
    
    
    fill(255,255,255)
    teethNum = 6
    for i in range(teethNum):
        angle = i * PI/teethNum
        pushMatrix()
        translate(-35*sin(angle),-35*cos(angle),0)
        rotateY(PI/2)
        rotateX(angle-PI/2)
        scale(12,12,1)
        cylinder(3)
        popMatrix()
    popMatrix()
    
def bottomClamShell(time):
    pushMatrix()
    rotateX(-PI/2)
    rotateY(((sin(time*15) + 1) * PI/8)+PI/8)
    
    mySphere()
    mySphere(38, 160, 0, 32,6)
    
    fill(255,255,255)
    teethNum = 6
    for i in range(teethNum):
        angle = (((i+1)%teethNum) * PI/teethNum)+(PI/(2*teethNum))
        pushMatrix()
        translate(-37*sin(angle),-37*cos(angle),0)
        rotateY(PI/2)
        rotateX(angle-PI/2)
        scale(12,12,1)
        cylinder(3)
        popMatrix()
        
    popMatrix()

def drawEyes():
    eyeDist = 31.5
    
    pushMatrix()
    translate(cos(5*PI/4)*eyeDist,cos(5*PI/4)*eyeDist,sin(PI/4)*eyeDist)
    fill(255,255,255)
    rotateX(5.1*PI/4)
    rotateY(-3.3*PI/4)
    scale(8,8,1)
    mySphere(1, 255, 255, 255,6)
    
    pushMatrix()
    translate(0,0,1)
    mySphere(0.5, 0, 0, 0,6)
    popMatrix()
    
    popMatrix()
    
    pushMatrix()
    eyeDist = 32
    translate(cos(5*PI/4)*eyeDist,-cos(5*PI/4)*eyeDist,sin(PI/4)*eyeDist)
    
    fill(255,255,255)
    rotateX(3*PI/4)
    rotateY(-3.3*PI/4)
    scale(8,8,1)
    mySphere(1, 255, 255, 255,6)
    
    pushMatrix()
    translate(0,0,1)
    mySphere(0.5, 0, 0, 0,6)
    popMatrix()
    
    popMatrix()
    
        

    
        
def chain(numLinks=5):
    fill(211,211,211)
    # Creating end cap
    ## End link
    pushMatrix()
    translate(0,0,0)
    rotateY(numLinks*PI/2)
    rotateZ(PI)
    torus(half=True)
    
    ## End cylinders
    pushMatrix()
    translate(1,-0.5,0)
    rotateX(PI/2)
    scale(0.5,0.5,0.5)
    cylinder(6,False)
    popMatrix()
    
    pushMatrix()
    translate(-1,-0.5,0)
    rotateX(PI/2)
    scale(0.5,0.5,0.5)
    cylinder(6,False)
    popMatrix()
    
    ## End cap
    pushMatrix()
    translate(0,-1.5,0)
    rotateX(PI/2)
    scale(2,2,0.5)
    cylinder(8)
    popMatrix()
    
    
    
    # Create all the individual chain links
    for linkNum in range(numLinks):
        
        pushMatrix()
        translate(0,(linkNum+0.5)*2.75,0)
        rotateY((linkNum+1)*PI/2)
        if(linkNum == 0):
            rotateX(PI/4)
        chainlink()
        popMatrix()
     
    popMatrix()

def chainlink():
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
    
    # Side cylinders
    pushMatrix()
    translate(1,0,0)
    rotateX(PI/2)
    scale(0.5,0.5,1)
    cylinder(6,False)
    popMatrix()
    
    pushMatrix()
    translate(-1,0,0)
    rotateX(PI/2)
    scale(0.5,0.5,1)
    cylinder(6,False)
    popMatrix()
    
    
