#include <IRremote.h>

#define IR_RECEIVE_PIN 3

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN);
  Serial.println("IR loopback running");
}

void loop() {
  Serial.println("Sending 0x55");
  IrSender.sendNEC(0x00, 0x55, 3);   // address, command, repeats

  delay(100);

  if (IrReceiver.decode()) {
    Serial.print("Received: 0x");
    Serial.println(IrReceiver.decodedIRData.command, HEX);
    IrReceiver.resume();
  } else {
    Serial.println("No data received");
  }

  Serial.println("------");
  delay(2000);
}
