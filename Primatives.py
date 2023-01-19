# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50, cap = True):
    if (cap):
        # first endcap
        beginShape()
        for i in range(sides):
            theta = i * 2 * PI / sides
            x = cos(theta)
            y = sin(theta)
            vertex ( x,  y, -1)
        endShape(CLOSE)
        # second endcap
        beginShape()
        for i in range(sides):
            theta = i * 2 * PI / sides
            x = cos(theta)
            y = sin(theta)
            vertex ( x,  y, 1)
        endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

# Draw a torus flat in the XY plane
def torus(radius=1.0, tube_radius=0.5, detail_x=16, detail_y=16, half = False):
    radius = float(radius)
    tube_radius = float(tube_radius)
    detail_x = int(detail_x)
    detail_y = int(detail_y)

    tube_ratio = (tube_radius / radius)

    def make_torus():
        vertices = []
        normals = []
        for torus_segment in range(detail_x):
            theta = 2 * PI * torus_segment / detail_x
            cos_theta = cos(theta)
            sin_theta = sin(theta)

            segment_vertices = []
            segment_normals = []

            for tube_segment in range(detail_y):
                phi = 2 * PI * tube_segment / detail_y
                cos_phi = cos(phi)
                sin_phi = sin(phi)
                segment_vertices.append(PVector(
                    cos_theta * (radius + cos_phi * tube_radius),
                    sin_theta * (radius + cos_phi * tube_radius),
                    sin_phi * tube_radius,
                ))
                segment_normals.append(PVector(
                    cos_phi * cos_theta,
                    cos_phi * sin_theta,
                    sin_phi,
                ))
            vertices.append(segment_vertices)
            normals.append(segment_normals)
        return vertices, normals

    global GEOMETRY_CACHE
    try:
        GEOMETRY_CACHE
    except NameError:
        GEOMETRY_CACHE = {}
    cache_index = ("torus", radius, tube_radius, detail_x, detail_y)
    if cache_index in GEOMETRY_CACHE:
        vertices, normals = GEOMETRY_CACHE[cache_index]

    else:
        vertices, normals = make_torus()
        GEOMETRY_CACHE[cache_index] = (vertices, normals)
    
    loopx = detail_x
    if (half):
        loopx = int(detail_x/2)
    for i in range(loopx):
        for j in range(detail_y):
            beginShape()

            normal(normals[i][j].x, normals[i][j].y, normals[i][j].z)
            vertex(vertices[i][j].x, vertices[i][j].y, vertices[i][j].z)
            normal(normals[(i + 1) % detail_x][j].x, normals[(i + 1) % detail_x][j].y, normals[(i + 1) % detail_x][j].z)
            vertex(vertices[(i + 1) % detail_x][j].x, vertices[(i + 1) % detail_x][j].y, vertices[(i + 1) % detail_x][j].z)
            normal(normals[(i + 1) % detail_x][(j + 1) % detail_y].x, normals[(i + 1) % detail_x][(j + 1) % detail_y].y, normals[(i + 1) % detail_x][(j + 1) % detail_y].z)
            vertex(vertices[(i + 1) % detail_x][(j + 1) % detail_y].x, vertices[(i + 1) % detail_x][(j + 1) % detail_y].y, vertices[(i + 1) % detail_x][(j + 1) % detail_y].z)
            normal(normals[i][(j + 1) % detail_y].x, normals[i][(j + 1) % detail_y].y, normals[i][(j + 1) % detail_y].z)
            vertex(vertices[i][(j + 1) % detail_y].x, vertices[i][(j + 1) % detail_y].y, vertices[i][(j + 1) % detail_y].z)

            endShape(CLOSE)
            
            
def mySphere(r=40, R=0, G=0, B=0, total=10):
    def makeSphere():
        globe = []
        for i in range(total+1):
            layerVertices = []
            lat = map(i, 0, total, 0, PI)
            for j in range(total+1):
                lon = map(j, 0, total, 0, TWO_PI)
                x = r * sin(lat) * cos(lon)
                y = r * sin(lat) * sin(lon)
                z = r * cos(lat)
                layerVertices.append(PVector(x, y, z))
            globe.append(layerVertices)
            
        return globe
        
    global GEOMETRY_CACHE
    try:
        GEOMETRY_CACHE
    except NameError:
        GEOMETRY_CACHE = {}
    cache_index = ("mysphere", r, total)
    if cache_index in GEOMETRY_CACHE:
        globe = GEOMETRY_CACHE[cache_index]

    else:
        globe = makeSphere()
        GEOMETRY_CACHE[cache_index] = globe

    for i in range(int((total+1)/2)):
        fill(R,G,B)
        beginShape(TRIANGLE_STRIP)
        for j in range(total+1):
            v1 = globe[i][j]
            vertex(v1.x, v1.y, v1.z)
            v2 = globe[i+1][j]
            vertex(v2.x, v2.y, v2.z)
    
        endShape()
        
def mySphere2(r=40, R=0, G=0, B=0, total=10):
    def makeSphere():
        globe = []
        for i in range(total+1):
            layerVertices = []
            lat = map(i, 0, total, 0, PI)
            for j in range(total+1):
                lon = map(j, 0, total, 0, TWO_PI)
                x = r * sin(lat) * cos(lon)
                y = r * sin(lat) * sin(lon)
                z = r * cos(lat)
                layerVertices.append(PVector(x, y, z))
            globe.append(layerVertices)
            
        return globe
        
    global GEOMETRY_CACHE
    try:
        GEOMETRY_CACHE
    except NameError:
        GEOMETRY_CACHE = {}
    cache_index = ("mysphere", r, total)
    if cache_index in GEOMETRY_CACHE:
        globe = GEOMETRY_CACHE[cache_index]

    else:
        globe = makeSphere()
        GEOMETRY_CACHE[cache_index] = globe

    for i in range(int((3*total+1)/4)):
        fill(R,G,B)
        beginShape(TRIANGLE_STRIP)
        for j in range(total+1):
            v1 = globe[i][j]
            vertex(v1.x, v1.y, v1.z)
            v2 = globe[i+1][j]
            vertex(v2.x, v2.y, v2.z)
    
        endShape()
