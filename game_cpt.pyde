# Template for Processing sketches.
# Map 
img = none

def setup():
    size(1000, 500)
    global img
img = create
img = createGrapics(width/4, height/4)
img.beginDraw()
img.background(0)
img.fill(255, 0, 0) 
tank = PVector(400, 400)
turn = 0
speed = 0
#Moving tank
moveUp = False
moveBack = False
turnCCW = False
turnCW = False

def draw():
    global img
    global speed
    global turn
    global tank
    #Move tank
    global moveUp
    global moveBack
    global turnCCW
    global turnCW

    background(255)
    image(img, 50, 50)
    fill(0, 255, 0)
   
    translate(tank.x, tank.y)
    rotate(radians(turn))
    fill(0, 255, 0)
    rect(-20, -20, 40, 40)
    rect(-20, -15, 40, 30)
    rect(0, -5, 30, 10)
   
    fill(0, 255, 0)
    ellipse(0, 0, 25, 25)
    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)
    if tank.x >= 1000 :
        tank.x = 999
        turn += 180
    elif tank.x <= 0:
        tank.x = 1
        turn += 180
    elif moveUp == True:
        tank.add(speed)
    elif moveBack == True:
        tank.sub(speed)
    if tank.y >= 500 or tank.y <= 0:
        turn *= -1
    elif turnCCW == True:
        turn -= 4
    elif turnCW == True:
        turn += 4
def keyPressed():
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    if key == "w":
        moveUp = True
        moveBack = False
    if key == "s":
        moveBack = True
        moveUp = False
    if key == "a":
        turnCCW = True
        turnCW = False
    if key == "d":
        turnCW = True
        turnCCW = False
def keyReleased():
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    if key == "w":
        moveUp = False
    if key == "s":
        moveBack = False
    if key == "a":
        turnCCW = False
    if key == "d":
        turnCW = False