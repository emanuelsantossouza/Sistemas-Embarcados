void setup()
{
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop()
{
  digitalWrite(8, HIGH);
  digitalWrite(7, HIGH);
  delay(1000);
  digitalWrite(8, LOW);
  digitalWrite(7, LOW);
  delay(1000);
}
