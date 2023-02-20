#include <Servo.h>
Servo servoX;
Servo servoY;
int speed =1;
int posX =0 ,posY = 0;
int inByte;
void setup() 
{ 
  Serial.begin(9600);
  servoX.attach(9);
  servoY.attach(10);
} 

void loop(){
    if (Serial.available() > 0){
        inByte = Serial.read();
        switch (inByte){
            case 'U':
                posY +=speed;
                break;
            case 'D':
                posY -=speed;
                break;
            case 'L':
                posX +=speed;
                break;
            case 'R':
                posY -=speed;
                break;
            case 'H':
                posX = 0;
                posY = 0;
                break;
            case 'F':
                if (speed <5){
                    speed +=1;
                } 
                break;
            case 'S':
                if (speed >1){
                    speed -=1;
                }
                break;
            default:
                break;
        }
        if (posY <0){
            posY =0;
        }else if(posY >180){
            posY = 180;
        }
        if (posX < 0){
            posX =0;
        }else if(posX >180){
            posX = 180;
        }
        servoX.write(posX);
        servoY.write(posY);
        Serial.print("C");//complete
        inByte = 0;
    }
}