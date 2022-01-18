var w;

function setup() {
  createCanvas(400, 400);
  // Make a Walker object
  w = new Walker();
}

function draw() {
  
  if (mouseIsPressed) {
    background(0);
  }
  // Update and display object
  w.update();
  w.display();
}

function Walker() {

  this.update = function() {
    // Move Walker randomly
    this.pos = createVector(mouseX, mouseY);
  }

  this.display = function() {
    // Draw Walker as circle
    if (key == 'r') {
      fill(255, 0, 0);
    }
    if (key == 'g') {
      fill(0, 255, 0);
    }
    if (key == 'b') {
      fill(0, 0, 255);
    }
    if (key == 'a') {
      fill(random(255), random(255), random(255));
    }
    ellipse(this.pos.x, this.pos.y, 30, 30);
  }
}
