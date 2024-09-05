#include "DHT.h"

#define DHTPIN 21      // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
#define LEDPIN 10
DHT dht(DHTPIN, DHTTYPE);

// Teensy 5V <--> HC-05 Vcc
// Teensy Ground <--> HC-05 GND
#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

void setup() {
  // Setup DHT Sensor
  pinMode(DHTPIN, INPUT);
  dht.begin();

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
  int sensorValue = analogRead(DHTPIN);
  //Serial.print(sensorValue);
  //Serial1.print(sensorValue);
  if (sensorValue > 150) {
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(LEDPIN, HIGH);
    Serial.print("HIGH\n");
    Serial1.print("HIGH\n");
  }
  else {
    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(LEDPIN, LOW);
    Serial.print("LOW\n");
    Serial1.print("LOW\n");
  }
  delay(1000);
}