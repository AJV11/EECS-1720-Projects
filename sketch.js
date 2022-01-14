var w;

function setup() {
  createCanvas(400, 400);
  // Make a Walker object
  w = new Walker();
}

function draw() {
  background(255, 166, 0);
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
    fill(random(255), random(255), random(255));
    ellipse(this.pos.x, this.pos.y, 50, 50);
  }
}
