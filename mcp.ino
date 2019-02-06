#include<Servo.h>
int angle=40;
Servo servo;
int sensorValue;
int ldrValue;
int LDR=4;
int led=2;
int fan=3;
int val=1;

void setup()
{
  servo.attach(8);
  servo.write(angle);
Serial.begin(9600);      // sets the serial port to 9600
pinMode(led, OUTPUT);
pinMode(fan,OUTPUT);
pinMode(LDR,INPUT);
}
void loop()
{
Serial.println("-------------------");
sensorValue = analogRead(A0);

Serial.println(sensorValue);// read analog input pin 0
delay(500);// wait 100ms for next reading

if(sensorValue>=200)
{digitalWrite(led,HIGH);
delay(2000);
digitalWrite(led,LOW);
delay(1000);
digitalWrite(fan,HIGH);
delay(5000);
digitalWrite(fan,LOW);
delay(100);
}
ldrValue=digitalRead(LDR);
Serial.println(ldrValue);
delay(300); 

if(ldrValue==1)
{
  for(angle=0;angle<40;angle++)
  {
    servo.write(angle);
    delay(50);
  }
  delay(1000);
  for(angle=40;angle>0;angle--)
  {
    servo.write(angle);
    delay(50);
  }
}
  
}
