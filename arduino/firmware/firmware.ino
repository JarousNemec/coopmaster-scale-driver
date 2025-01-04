#include "Arduino.h"

#include "HX711.h"

#define DOUT 2
#define CLK 3

HX711 scale(DOUT, CLK);
float calibration_factor = -9555;  //This value is obtained with experiences
float lbs_to_kg = 2.20462262;
byte weigth_samples = 1;
float last_zero_value = 0;
float robot_weight = 1.557;
float current_weight = 0;
float current_weight_package = 0;

void setup() {
  Serial.begin(9600);
  scale.set_scale(calibration_factor);
  //scale.set_scale(0);
  scale.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
}

void loop() {
  //Serial.println(scale.get_units()/2.2, 4);
  //if (Serial.available() > 0) {
  char c = Serial.read();  //gets one byte from serial buffer
  //Serial.println(scale.get_units()/lbs_to_kg, 4);
  current_weight = scale.get_units(weigth_samples) / lbs_to_kg;
  if (current_weight < robot_weight) {
    last_zero_value = current_weight;
  }
  if (c == 'w') {
    current_weight_package = scale.get_units(weigth_samples) / lbs_to_kg - last_zero_value;
    Serial.println(current_weight_package, 4);
    //weight_package = scale.get_units(weigth_samples)/lbs_to_kg, 4;
    //Serial.println(scale.get_units(weigth_samples)/lbs_to_kg, 4);
  }
  if (c == 'a') {
    scale.set_scale(calibration_factor);
    scale.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
  }
  if (c == '+') {
    calibration_factor = calibration_factor + 10;
    scale.set_scale(calibration_factor);
    //scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
  }
  if (c == '-') {
    calibration_factor = calibration_factor - 10;
    scale.set_scale(calibration_factor);
    //scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
  }
  if (c == '/') {
    calibration_factor = calibration_factor + 100;
    scale.set_scale(calibration_factor);
    //scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
  }
  if (c == '=') {
    calibration_factor = calibration_factor - 100;
    scale.set_scale(calibration_factor);
    //scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
  }
  if (c == 't') {
    scale.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
  }
  if (c == 'f') {
    Serial.println(calibration_factor);
  }
  //}
}
