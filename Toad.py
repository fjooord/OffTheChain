from Primatives import *

def drawToad(time=0):
    pushMatrix()
    translate(0,-20,0)
    rotateY(PI/4)
    DrawHat()
    popMatrix()
    
    DrawHead()
    
    # Draw Torso
    pushMatrix()
    translate(0,5,0)
    scale(1,1.2,1)
    fill(0,0,240)
    sphere(10)
    popMatrix()
    
   
    DrawLegs(time)
    DrawArms(time)
    
    
def DrawArms(time):
    #Draw arms
    pushMatrix()
    translate(0,-5,5)
    rotateZ(((sin(time*5)) * PI/4))
    pushMatrix()
    translate(0,5,6)
    rotateX(PI/4)
    scale(.8,1.6,.8)
    fill(101,67,33)
    sphere(4)
    popMatrix()
    popMatrix()
    
    pushMatrix()
    translate(0,-5,-5)
    rotateZ(-((sin(time*5)) * PI/4))
    pushMatrix()
    translate(0,5,-6)
    rotateX(-PI/4)
    scale(0.8,1.6,0.8)
    fill(101,67,33)
    sphere(4)
    popMatrix()
    popMatrix()

def DrawLegs(time):
     # Draw Legs
    pushMatrix()
    # Create a 2 layer matrix to be abel to have the legs move with the first matirx as the pivot point
    translate(0,13,6)
    rotateZ(((sin(time*5)) * PI/4))
    pushMatrix()
    translate(0,3,0)
    rotateZ(PI/2)
    scale(1,1.2,1)
    fill(101,67,33)
    sphere(4)
    popMatrix()
    popMatrix()
    
    pushMatrix()
    translate(0,13,-6)
    rotateZ(-((sin(time*5)) * PI/4))
    pushMatrix()
    translate(0,3,0)
    rotateZ(PI/2)
    scale(1,1.2,1)
    fill(101,67,33)
    sphere(4)
    popMatrix()
    popMatrix()
    
def DrawHead():
    pushMatrix()
    fill(232,190,172)
    translate(0,-15,0)
    rotateX(PI/2)
    scale(7,7,5)
    cylinder(8, False)
    popMatrix()
    
    pushMatrix()
    translate(0,-10,0)
    rotateX(-PI/2)
    mySphere(7, 232,190,172,8)
    
    pushMatrix()
    translate(5.5,2,0)
    rotateX(-PI/2)
    rotateY(0.9*PI/2)
    scale(1,1.4,1)
    mySphere(2, 0,0,0,4)
    popMatrix()
    
    pushMatrix()
    translate(5.5,-2,0)
    rotateX(-PI/2)
    rotateY(1.1*PI/2)
    scale(1,1.4,1)
    mySphere(2, 0,0,0,4)
    popMatrix()
    
    popMatrix()
    
def DrawHat():
    pushMatrix()
    
    rotateX(PI/2)
    mySphere2(10, 255,255,255,8)

    
    pushMatrix()
    translate(6,-6,0)
    rotateX(PI/2)
    rotateY(PI/4)
    mySphere(3, 255,0,0,6)
    popMatrix()
    
    pushMatrix()
    translate(-6, 6,0)
    rotateX(-PI/2)
    rotateY(-PI/4)
    mySphere(3, 255,0,0,6)
    popMatrix()
    
    pushMatrix()
    translate(-6, -6,0)
    rotateX(PI/2)
    rotateY(-PI/4)
    mySphere(3, 255,0,0,6)
    popMatrix()
    
    pushMatrix()
    translate(6, 6,0)
    rotateX(-PI/2)
    rotateY(PI/4)
    mySphere(3, 255,0,0,6)
    popMatrix()
    
    popMatrix()
