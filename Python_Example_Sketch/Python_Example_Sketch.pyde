add_library('sound')

c1, c2, ch1, ch2 = None, None, None, None


def setup():  
    size(1200, 800)
    smooth()
    
    global c1, c2
    c1 = color(random(255), random(255), random(255))
    c2 = color(random(255), random(255), random(255))
    
    global ch1, ch2
    ch1 = SinOsc(this)
    ch1.play(0, 1)
    ch2 = SinOsc(this)
    ch2.play(0, 1)
    
    
def draw():
    global c1, c2, ch1, ch2
    background(0)
    stroke(0)
    noFill()
    constantFactor = 1.1
    circleSize = 10
    
    if mousePressed:
        ch1.set(250, 1, 0, 0)
        ch2.set(250, 1, 0, 0)
        
        for i in range(0, 30):
            p = lerpColor(c1, c2, 1.0*i/width)
            stroke(p)
            strokeWeight(circleSize/25.0)
            
            ellipse(200, 100, circleSize, circleSize)
            ellipse(600, 100, circleSize, circleSize)
            ellipse(1000, 100, circleSize, circleSize)
            
            ellipse(200, 400, circleSize, circleSize)
            ellipse(600, 400, circleSize, circleSize)
            ellipse(1000, 400, circleSize, circleSize)
            
            ellipse(200, 700, circleSize, circleSize)
            ellipse(600, 700, circleSize, circleSize)
            ellipse(1000, 700, circleSize, circleSize)
            circleSize = circleSize * constantFactor
            
    else:
        ch1.set(0, 1, 0, 0)
        ch2.set(0, 1, 0, 0)
        
        
def mousePressed():
    global c1, c2
    c1 = color(random(255), random(255), random(255))
    c2 = color(random(255), random(255), random(255))
    ch1.set(250, 1, 0, 0)
    ch2.set(250, 1, 0, 0)
