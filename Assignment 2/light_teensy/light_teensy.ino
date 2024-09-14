#include "DHT.h"

#define DHTPIN 21      // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11  // DHT 11
#define LEDPIN 10
DHT dht(DHTPIN, DHTTYPE);

bool manualMode = false;
#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

void handleLighting(bool turnOn) {
  if (turnOn) {
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(LEDPIN, HIGH);
    Serial.println("HIGH");
    Serial1.println("HIGH");
  } else {
    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(LEDPIN, LOW);
    Serial.println("LOW");
    Serial1.println("LOW");
  }
}

void autoLighting(int sensorValue, String str) {
  if (!manualMode) {
    // Automatic mode logic
    if (sensorValue > 400) {
      handleLighting(false);
    } else {
      handleLighting(true);
    }

    // Check for "MANUAL" in the string
    if (str.indexOf("MANUAL") >= 0) {
      manualMode = true;
    }

    // Check for "AUTO" in the string
    if (str.indexOf("AUTO") >= 0) {
      manualMode = false;
    }

    Serial.println("Sensor Value: " + String(sensorValue));
    Serial.println("Manual Mode: " + String(manualMode));
  } else {
    // Manual mode logic
    if (str.equals("Light ON")) {
      handleLighting(true);
    } else if (str.equals("Light OFF")) {
      handleLighting(false);
    }

    // Check for "MANUAL" in the string
    if (str.indexOf("MANUAL") >= 0) {
      manualMode = true;
    }

    // Check for "AUTO" in the string
    if (str.indexOf("AUTO") >= 0) {
      manualMode = false;
    }

    Serial.println("Manual Mode: " + String(manualMode));
  }
}

void setup() {
  // Setup DHT Sensor
  pinMode(DHTPIN, INPUT);
  dht.begin();

  // Setup Serial1 for BlueTooth
  Serial.begin(9600);
  Serial1.begin(9600); // Default communication rate of the Bluetooth module
  pinMode(LEDPIN, OUTPUT);
}

void loop() {
  int sensorValue = analogRead(DHTPIN);

  if (Serial1.available() > 0) {
    String str = Serial1.readString().trim();  // Read and trim input
    Serial.println("Received: " + str);

    // Check for "MANUAL" or "AUTO" in the string
    if (str.indexOf("MANUAL") >= 0) {
      manualMode = true;
    }
    if (str.indexOf("AUTO") >= 0) {
      manualMode = false;
    }

    autoLighting(sensorValue, str);
  }
}
