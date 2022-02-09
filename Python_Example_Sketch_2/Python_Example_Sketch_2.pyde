add_library('sound')

numRings = 500
ring = [0] * numRings
currentRing = 0
colour, ch1, ch2 = None, None, None


def setup():
    global numRings, ring, ch1, ch2
    size(1000, 800)
    smooth()
    
    for i in range(numRings):
        colour = color(random(255), random(255), random(255))
        ring[i] = Ring(0, 0, 0, False, colour)
    
    ch1 = SinOsc(this)
    ch1.play(0, 1)
    ch2 = SinOsc(this)
    ch2.play(0, 1)

def draw():
    global numRings, ring
    time = radians(frameCount)
    colorMode(HSB)
    background(255*(.5+.5*cos(time)),255*(.5+.5*cos(time)),255*(.5+.5*cos(time)))
    
    for i in range(numRings):
        ring[i].grow()
        ring[i].display()
        
    if mousePressed:
        ch1.set(300, 1, 0, 0)
        ch2.set(300, 1, 0, 0)
    else:
        ch1.set(0, 1, 0, 0)
        ch2.set(0, 1, 0, 0)
    
    
def mousePressed():
    global numRings, ring, currentRing
    
    ring[currentRing].start(mouseX, mouseY)
    currentRing += 1
    if (currentRing >= numRings):
        currentRing = 0
        
    
class Ring(object):
    def __init__(self, x, y, diameter, on, colour):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.on = False
        self.colour = colour
    
    def start(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.on = True
        self.diameter = 1
        
    def grow(self):
        if (self.on == True):
            self.diameter += 10.0
            if (self.diameter > 800):
                self.on = False
        
    def display(self):
        if (self.on == True):
            noFill()
            strokeWeight(5)
            stroke(self.colour)
            ellipse(self.x, self.y, self.diameter, self.diameter)
