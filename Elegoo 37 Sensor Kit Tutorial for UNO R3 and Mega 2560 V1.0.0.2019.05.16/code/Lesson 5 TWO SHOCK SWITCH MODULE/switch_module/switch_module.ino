/******************************************
  Website: www.elegoo.com

  Time:2017.12.12

 ******************************************/

int Led = 13; //define LED port
int buttonpin = 3; //define switch port
int  val;//define digital variable val
int led_state = 0;

void  setup()
{
  Serial.begin(9600);
  pinMode(Led, OUTPUT); //define LED as a output port
  pinMode(buttonpin, INPUT); //define switch as a output port
  digitalWrite(buttonpin, LOW);
}
void  loop()
{
  val = digitalRead(buttonpin); //read the value of the digital interface 3 assigned to val
  if (val == LOW)
  {
    delay(20);
    led_state = !led_state;
    digitalWrite(Led, led_state);
//    Serial.println("detect shock!");   
  }
}
