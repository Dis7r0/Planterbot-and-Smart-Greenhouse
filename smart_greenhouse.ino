#include "DHT.h"
#define DHTPIN 2 
#define DHTTYPE DHT11 
const int relay = 8;
const int moisture1 = A0;
const int moisture2 = A1;
const int ldrPin = A4;    //"S" is data pin. Middle is Vcc. "-" is Gnd.
unsigned long startMillis;
unsigned long currentMillis;
const unsigned long period = 2000;
DHT dht(DHTPIN, DHTTYPE);
const int motor1pin1 = 11; //In1
const int motor1pin2 = 12; //In2
const int enable1 = 10;


void setup() {
  // put your setup code here, to run once:
  pinMode(relay, OUTPUT);
  pinMode(ldrPin, INPUT);
  pinMode(moisture1, INPUT);
  pinMode(moisture2, INPUT);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(enable1, OUTPUT);
  digitalWrite(relay, LOW);
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));
  dht.begin();
  startMillis = millis();  //initial start time
}

void loop() {
  // put your main code here, to run repeatedly:
  currentMillis = millis(); //get the current "time" (actually the number of milliseconds since the program started)
  
  int ldr = analogRead(ldrPin);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int m1 = analogRead(moisture1);
  int m2 = analogRead(moisture2);
  if(ldr>450){
    digitalWrite(relay, LOW);
    Serial.println("Light is ON!");
    delay(3000);
    }
  else{
    digitalWrite(relay, HIGH);
    //Serial.println("Light OFF");
  }

  if(t>30.4){
    analogWrite(enable1, 100);
    digitalWrite(motor1pin1, HIGH);
    digitalWrite(motor1pin2, LOW);
    Serial.println("Fan is ON!");
    delay(3000);
    }
  else{
    analogWrite(enable1,0);
    digitalWrite(motor1pin1, LOW);
    digitalWrite(motor1pin2, LOW);
    }
 
  if (currentMillis - startMillis >= period)  //test whether the period has elapsed
 { Serial.print("Average Soil moisture = ");
   Serial.print((m1+m2)/2);
   Serial.print("\n");
   Serial.print("LDR value = ");
   Serial.print(ldr);
   Serial.print("\n");
   Serial.print(F("Humidity: "));
   Serial.print(h);
   Serial.print(F("%  Temperature: "));
   Serial.print(t);
   Serial.println(F("°C "));
   startMillis = currentMillis;  //IMPORTANT to save the start time of the current LED state.
 }
}
