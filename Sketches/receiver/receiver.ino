
const int IRPin = 2;       // Receiver Pin
const int irLedPin = 3;    // Transmitter Pin
const int statusLED = 13;  // Built-in LED


unsigned long lastBeamTime = 0;
const long limit = 100; // Trigger alarm 

void setup() {
  Serial.begin(9600);
  pinMode(IRPin, INPUT);
  pinMode(irLedPin, OUTPUT);
  pinMode(statusLED, OUTPUT);
  Serial.println("Combined Sensor Started");
}

void loop() {

  // Sende Signal 38kHz
  tone(irLedPin, 38000);
  //Umsetzungstoleranz
  delay(2); 

  // Lesen Sensor
  int sensorState = digitalRead(IRPin);

  //IR-Licht ausschalten
  noTone(irLedPin);

  if (sensorState == LOW) {
    lastBeamTime = millis(); // Reset timer
    digitalWrite(statusLED, LOW); // Safe status
  }


  // Kein Signal von Transmitter(d.h. Transmitter empfängt IR-Licht)
  if (millis() - lastBeamTime > limit) {
    Serial.println("OBJECT DETECTED!"); 
    digitalWrite(statusLED, HIGH); // Alarm status
  }
  else Serial.println(digitalRead(IRPin));

  // Resetdelay
  delay(20);
}