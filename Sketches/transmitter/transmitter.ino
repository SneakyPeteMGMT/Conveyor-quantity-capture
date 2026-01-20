// TRANSMITTER SKETCH
const int irLedPin = 3; // Connect IR LED Anode here (with resistor)

void setup() {
  pinMode(irLedPin, OUTPUT);
}

void loop() {
  // 1. Send 38kHz signal for 10 milliseconds
  tone(irLedPin, 38000);
  delay(5);
  
  // 2. Turn OFF for 20 milliseconds
  // This gap is REQUIRED for the receiver to reset its gain
  noTone(irLedPin); 
  delay(30);
}