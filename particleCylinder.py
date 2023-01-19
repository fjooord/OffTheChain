def makeDirections():
    directions = []
    for x in range(19):
        ringDirs = []
        for i in range(16):
            theta = (i + 1) * 2 * PI / 16
            x = cos(theta)
            y = sin(theta)
            partDir = []
            partDir.append(x * 2*(random(10)/100))
            partDir.append(y * 2*(random(10)/100))
            partDir.append((random(-10,10)/100))
            partDir.append(int(random(3)))
            
            ringDirs.append(partDir)
        directions.append(ringDirs)
    return directions
        
def shatterCylinder(time, explosionDirs):
    for x in range(18):
        pushMatrix()
        translate(0,0,-0.9 + (x*0.1))
        scale(0.5,0.5,1)
        
        x1 = 1
        y1 = 0
        for i in range(16):
            theta = (i + 1) * 2 * PI / 16
            x2 = cos(theta)
            y2 = sin(theta)
            pushMatrix()
            
            #translate(x1,y1,0)
            translate(explosionDirs[x][i][0] * time * 5, explosionDirs[x][i][1] * time *5, explosionDirs[x][i][2] * time *5)
            
            pushMatrix()
            speedMult = 3
  
            if (explosionDirs[x][i][3] == 0):
                rotateX(time*speedMult)
            if (explosionDirs[x][i][3] == 1):
                rotateY(time*speedMult)
            if (explosionDirs[x][i][3] == 2):
                rotateZ(time*speedMult)
        
     
            beginShape()
    
            normal (x1, y1, 0)
            vertex (x1, y1, .1)
            vertex (x1, y1, -.1)
            normal (x2, y2, 0)
            vertex (x2, y2, -.1)
            vertex (x2, y2, .1)
            
            endShape(CLOSE)
            
            popMatrix()
            
            
            popMatrix()
            x1 = x2
            y1 = y2
        
        popMatrix()
