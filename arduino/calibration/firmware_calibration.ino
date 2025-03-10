#include "Arduino.h"

#include "HX711.h"

#define DOUT 3
#define CLK 2

//web tutorial with documentation: https://randomnerdtutorials.com/arduino-load-cell-hx711/

HX711 scale;

// void setup() {
//   Serial.begin(9600);
//   scale.begin(DOUT, CLK);
// }

// void loop() {

//   if (scale.is_ready()) {
//     scale.set_scale();
//     Serial.println("Tare... remove any weights from the scale.");
//     delay(5000);
//     scale.tare();
//     Serial.println("Tare done...");
//     Serial.print("Place a known weight on the scale...");
//     delay(5000);
//     long reading = scale.get_units(10);
//     Serial.print("Result: ");
//     Serial.println(reading);
//   }
//   else {
//     Serial.println("HX711 not found.");
//   }
//   delay(1000);
// }


void setup() {
  Serial.begin(9600);
  Serial.println("HX711 Demo");
  Serial.println("Initializing the scale");

  scale.begin(DOUT, CLK);

  Serial.println("Before setting up the scale:");
  Serial.print("read: \t\t");
  Serial.println(scale.read());      // print a raw reading from the ADC

  Serial.print("read average: \t\t");
  Serial.println(scale.read_average(20));   // print the average of 20 readings from the ADC

  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight (not set yet)

  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);  // print the average of 5 readings from the ADC minus tare weight (not set) divided
            // by the SCALE parameter (not set yet)

  scale.set_scale(-100.935);
  //scale.set_scale(-471.497);                      // this value is obtained by calibrating the scale with known weights; see the README for details
  scale.tare();               // reset the scale to 0

  Serial.println("After setting up the scale:");

  Serial.print("read: \t\t");
  Serial.println(scale.read());                 // print a raw reading from the ADC

  Serial.print("read average: \t\t");
  Serial.println(scale.read_average(20));       // print the average of 20 readings from the ADC

  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight, set with tare()

  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);        // print the average of 5 readings from the ADC minus tare weight, divided
            // by the SCALE parameter set with set_scale

  Serial.println("Readings:");
}

void loop() {
  Serial.print("one reading:\t");
  Serial.print(scale.get_units(), 1);
  Serial.print("\t| average:\t");
  Serial.println(scale.get_units(10), 5);

  delay(5000);
}