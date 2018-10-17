const int pwm1 = 3;
const int pwm2 = 4;
const int pwm3 = 5;
const int pwm4 = 6;
//const int buzzerPin = 24;

long sensor;
//long test;

void setup() {
Serial.begin(9600);
pinMode(pwm1, INPUT);
pinMode(pwm2, INPUT);
pinMode(pwm3, INPUT);
pinMode(pwm4, INPUT);
//pinMode(buzzerPin, OUTPUT);
}

void read_sensor (){
//test = pulseIn(pwm1, HIGH);
/*sensor = pulseIn(pwm1, HIGH);
sensor.concat("#");
sensor.concat(pulseIn(pwm2, HIGH));
sensor.concat("#");
sensor.concat(pulseIn(pwm3, HIGH));
sensor.concat("#");
sensor.concat(pulseIn(pwm4, HIGH));*/
}

void print_range(){
sensor = pulseIn(pwm1, HIGH);
Serial.print(sensor);
Serial.print("#");

sensor = pulseIn(pwm2, HIGH);
Serial.print(sensor);
Serial.print("#");

sensor = pulseIn(pwm3, HIGH);
Serial.print(sensor);
Serial.print("#");

sensor = pulseIn(pwm4, HIGH);
Serial.print(sensor);
Serial.print(" ");
}

void loop() { 
//read_sensor();
print_range();
/*if(test < 5000)
{
digitalWrite (buzzerPin, HIGH);
}
else
{
digitalWrite (buzzerPin, LOW);
}
*/
delay(100);


}
