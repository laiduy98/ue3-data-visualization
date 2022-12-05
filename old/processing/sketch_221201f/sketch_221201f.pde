// Need G4P library
import g4p_controls.*;
// You can remove the PeasyCam import if you are not using
// the GViewPeasyCam control or the PeasyCam library.
import peasy.*;

import grafica.*;

public GPointsArray polygonPoints;
public GPlot plot1;

public PImage logoUniv;
public PImage mug;
public PShape star;


public void setup(){
  size(1050, 660, JAVA2D);
  createGUI();
  customGUI();
  // Place your setup code here
  
  logoUniv = loadImage("logo-univ.png");
  
  // Prepare the points for the first plot  
  GPointsArray points1a = new GPointsArray(500);
  GPointsArray points1b = new GPointsArray(500);
  GPointsArray points1c = new GPointsArray(500);

  for (int i = 0; i < 500; i++) {
    points1a.add(i, noise(0.1*i) + 1, "point " + i);
    points1b.add(i, noise(500 + 0.1*i) + 0.5, "point " + i);
    points1c.add(i, noise(1000 + 0.1*i), "point " + i);
  }

  // Create a polygon to display inside the plot  
  polygonPoints = new GPointsArray(5);
  polygonPoints.add(2, 0.15);
  polygonPoints.add(6, 0.12);
  polygonPoints.add(15, 0.3);
  polygonPoints.add(8, 0.6);
  polygonPoints.add(1.5, 0.5);

  // Setup for the first plot
  plot1 = new GPlot(this);
  plot1.setPos(200, 0);
  plot1.setXLim(1, 100);
  plot1.setYLim(0.1, 3);
  plot1.getTitle().setText("Multiple layers plot");
  plot1.getXAxis().getAxisLabel().setText("Time");
  plot1.getYAxis().getAxisLabel().setText("noise (0.1 time)");
  plot1.setLogScale("xy");
  plot1.setPoints(points1a);
  plot1.setLineColor(color(200, 200, 255));
  plot1.addLayer("layer 1", points1b);
  plot1.getLayer("layer 1").setLineColor(color(150, 150, 255));
  plot1.addLayer("layer 2", points1c);
  plot1.getLayer("layer 2").setLineColor(color(100, 100, 255));
  
  
  plot1.activatePanning();
  plot1.activateZooming(1.2, CENTER, CENTER);
  plot1.activatePointLabels();
  
  // Load some images and shapes to use later in the plots
  mug = loadImage("beermug.png");
  mug.resize(int(0.7*mug.width), int(0.7*mug.height));
  star = loadShape("star.svg");
  star.disableStyle();
  
}

public void draw(){
  background(255);
  
  image(logoUniv, 20, 10, width/10, height/15);

  // Draw the first plot
  plot1.beginDraw();
  plot1.drawBackground();
  plot1.drawBox();
  plot1.drawXAxis();
  plot1.drawYAxis();
  plot1.drawTopAxis();
  plot1.drawRightAxis();
  plot1.drawTitle();
  plot1.drawFilledContours(GPlot.HORIZONTAL, 0.05);
  plot1.drawPoint(new GPoint(65, 1.5), mug);
  plot1.drawPolygon(polygonPoints, color(255, 200));
  plot1.drawLabels();
  plot1.endDraw();
  
}

// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
