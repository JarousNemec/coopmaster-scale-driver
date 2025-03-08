#include "Arduino.h"

#include "HX711.h"

#define DOUT 3
#define CLK 2

HX711 scale;
float calibration_factor = -100.935; 
float current_weight = 0;

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);

  scale.set_scale(calibration_factor);

  scale.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
}

void loop() {

  char c = Serial.read(); //gets one byte from serial buffer

  current_weight = scale.get_units(1);

  if (c == 'w') {
    Serial.println(current_weight, 4);
  }
  else if (c == 't') {
    scale.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
  }
}
