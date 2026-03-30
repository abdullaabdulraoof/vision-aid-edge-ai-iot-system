#define echob 4
#define trigb 5
#define echot 6
#define trigt 7

long duration1;
float bottom;
long duration2;
float top;

void setup()
{
 Serial.begin(9600);
 pinMode(9,OUTPUT);
 pinMode(echob, INPUT);
 pinMode(trigb, OUTPUT);
 pinMode(echot, INPUT);
 pinMode(trigt, OUTPUT);
}

void loop()
{
  digitalWrite(trigb, LOW);
  delayMicroseconds(2);
  digitalWrite(trigb, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigb, LOW);

  duration1 = pulseIn(echob, HIGH);
  bottom = duration1 * 0.0344 / 2;

  digitalWrite(trigt, LOW);
  delayMicroseconds(2);
  digitalWrite(trigt, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigt, LOW);

  duration2 = pulseIn(echot, HIGH);
  top = duration2 * 0.0344 / 2;

  if(bottom > 30 || top <25)
  {
    digitalWrite(9,HIGH);
  }
  else
  {
    digitalWrite(9,LOW);
  }

  delay(500);
}
