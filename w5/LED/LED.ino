#define LEDPIN 11

void setup() {
  // Setup serial for monitor and Setup Serial1 for BlueTooth
  Serial.begin(9600);
  Serial1.begin(9600);

  pinMode(LEDPIN, OUTPUT);
}

void loop() {
  // Process commands from bluetooth first.
  int integer = 3;
  if(Serial1.available() > 0){
    String str = Serial1.readString();
    integer = atoi(str.c_str());
    //Serial.println(interger);
    //Serial.println("hello");
    Serial.println(str);
    if(integer == 1){
      digitalWrite(LEDPIN, HIGH);
      Serial.println("LED ON");
    }else if(integer == 0){
        digitalWrite(LEDPIN, LOW);
        Serial.println("LED OFF");
      }
  }
}

