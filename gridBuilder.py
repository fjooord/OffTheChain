class subGridCell():
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.maxSep = max(abs(self.endX-self.startX), abs(self.endY-self.startY))

def makeStreetGrid():
    gridDivX = 21
    gridDivY = 21
    gridStart = subGridCell(0,0,gridDivX,gridDivY)
    
    gridCells = [gridStart]
    
    minSpacing = 4
    
    numDivisions = 15
    
    for i in range(numDivisions):
        temp_arr = gridCells
        gridCells = subDivideCells(gridCells, minSpacing)
    
    for cell in gridCells:
        print(cell.startX, cell.startY, cell.endX, cell.endY)
    
    bools = []
    for x in range(gridDivY + 1):
        column = []
        for y in range(gridDivX + 1):
            column.append(0)
    
        bools.append(column)
    
    for cell in gridCells:
        for i in range(cell.startY, cell.endY+1):
            for j in range(cell.startX, cell.endX+1):
                if (i == cell.startY or i == cell.endY):
                    bools[i][j] = 1
                elif (j == cell.startX or j == cell.endX):
                    bools[i][j] = 1
    # for b in bools:
    #     #continue
    #     print(b)
    # print()
    # print()
    
    bool2 = []
    
    temp = [2] * (gridDivX+3)
    bool2.append(temp)

    for row in bools:
        newrow = []
        newrow.append(2)
        for val in row:
            newrow.append(val)
        newrow.append(2)
        bool2.append(newrow)
    bool2.append(temp)
    
    
    # for row in bool2:
    #     print(row)
    
    return bool2
        
def subDivideCells(gridCells, minSpacing):
    #print(len(gridCells))
    newCells = []
    
    maxDiv = -1
    div_index = -1
    for i in range(len(gridCells)):
        if (gridCells[i].maxSep > minSpacing):
            if (gridCells[i].maxSep > maxDiv):
                maxDiv = gridCells[i].maxSep
                div_index = i
                
    if (div_index == -1):
        print("fail")
        return gridCells
    
    for x in range(len(gridCells)):
        if (x == div_index):
            continue
        else:
            newCells.append(gridCells[x])
            
    #print(maxDiv)
    #print()
    #print("DI",div_index)
    div_cell = gridCells[div_index]
    print("Cell to divide",div_cell.startX, div_cell.startY, div_cell.endX, div_cell.endY)
    
    if (abs(div_cell.endX-div_cell.startX) >= minSpacing):
        if (abs(div_cell.endY-div_cell.startY) >= minSpacing):
            rand = random(1)
            if (rand > 0.5):
                # we use X
                newX = int(round(abs(div_cell.endX+div_cell.startX)/2))
                print("div on X")
                newCells.append(subGridCell(div_cell.startX, div_cell.startY, newX, div_cell.endY))
                newCells.append(subGridCell(newX, div_cell.startY, div_cell.endX, div_cell.endY))
            else:
                # we use y
                print("div on Y")
                newY = int(round(abs(div_cell.endY+div_cell.startY)/2))
                print("newY",newY)
                newCells.append(subGridCell(div_cell.startX, div_cell.startY, div_cell.endX, newY))
                newCells.append(subGridCell(div_cell.startX, newY, div_cell.endX, div_cell.endY))
        else:
            # we use X
            newX = int(round(abs(div_cell.endX+div_cell.startX)/2))
            newCells.append(subGridCell(div_cell.startX, div_cell.startY, newX, div_cell.endY))
            newCells.append(subGridCell(newX, div_cell.startY, div_cell.endX, div_cell.endY))
            print("div on X")
    elif (abs(div_cell.endY-div_cell.startY) >= minSpacing):
        # we use y
        print("div on Y")
        
        newY = int(round(abs(div_cell.endY+div_cell.startY)/2))
        print("newY",newY)
        newCells.append(subGridCell(div_cell.startX, div_cell.startY, div_cell.endX, newY))
        newCells.append(subGridCell(div_cell.startX, newY, div_cell.endX, div_cell.endY))

    return newCells
