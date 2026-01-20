# include <IRremote.h>
int RECV_PIN = 11; // define input pin on Arduino
IRrecv irrecv (RECV_PIN);
decode_results results;


pinMode(13, OUTPUT);


void setup()
{
Serial.begin (9600);
irrecv.enableIRIn (); // Start the receiver
}

void loop()
{
digitalWrite(13, HIGH); // turn the LED on (HIGH is the voltage level)
delay(1000); // wait for a second

if (irrecv.decode (& results))
{
Serial.println (results.value, HEX);
irrecv.resume (); // Receive the next value
}

digitalWrite(13, LOW); // turn the LED off by making thevoltage LOW
delay(1000); // wait for a second

if (irrecv.decode (& results))
{
Serial.println (results.value, HEX);
irrecv.resume (); // Receive the next value
}
}
