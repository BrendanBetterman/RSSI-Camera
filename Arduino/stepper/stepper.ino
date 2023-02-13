int stepperOne[] = {10,9,8,11};
int stepperTwo[] = {4,5,6,7};
int Pin0 = 8; 
int Pin1 = 9; 
int Pin2 = 10; 
int Pin3 = 11; 
int _step = 0; 
int _count = 0;
boolean dir = true;// gre
int incomingByte;  
void setup() 
{ 
  Serial.begin(9600);
  for(int pin =0; pin<4; pin++){
    pinMode(stepperOne[pin], OUTPUT);  
    pinMode(stepperTwo[pin], OUTPUT);  
  }
} 
void driveStep(bool motor[]){
    for (int mstep=0; mstep<=8; mstep++){
      if (motor[0]){
        step(stepperOne,mstep);
      }else if(motor[2]){
        int reverse[] = {stepperOne[2],stepperOne[1],stepperOne[0],stepperOne[3]}; 
        step(reverse,mstep);
      }
      if (motor[1]){
        step(stepperTwo,mstep);
      }else if(motor[3]){
        //reverse step
        int reverse[] = {stepperTwo[2],stepperTwo[1],stepperTwo[0],stepperTwo[3]}; 
        step(reverse,mstep);
      }
      delay(1); 
    }
}
void step(int pins[],int mstep){
  switch(mstep){ 
    case 0: 
      digitalWrite(pins[0], LOW);  
      digitalWrite(pins[1], LOW); 
      digitalWrite(pins[2], LOW); 
      digitalWrite(pins[3], HIGH); 
    break;  
    case 1: 
      digitalWrite(pins[0], LOW);  
      digitalWrite(pins[1], LOW); 
      digitalWrite(pins[2], HIGH); 
      digitalWrite(pins[3], HIGH); 
    break;  
    case 2: 
      digitalWrite(pins[0], LOW);  
      digitalWrite(pins[1], LOW); 
      digitalWrite(pins[2], HIGH); 
      digitalWrite(pins[3], LOW); 
    break;  
    case 3: 
      digitalWrite(pins[0], LOW);  
      digitalWrite(pins[1], HIGH); 
      digitalWrite(pins[2], HIGH); 
      digitalWrite(pins[3], LOW); 
    break;  
    case 4: 
      digitalWrite(pins[0], LOW);  
      digitalWrite(pins[1], HIGH); 
      digitalWrite(pins[2], LOW); 
      digitalWrite(pins[3], LOW); 
    break;  
    case 5: 
      digitalWrite(pins[0], HIGH);  
      digitalWrite(pins[1], HIGH); 
      digitalWrite(pins[2], LOW); 
      digitalWrite(pins[3], LOW); 
    break;  
      case 6: 
      digitalWrite(pins[0], HIGH);  
      digitalWrite(pins[1], LOW); 
      digitalWrite(pins[2], LOW); 
      digitalWrite(pins[3], LOW); 
    break;  
    case 7: 
      digitalWrite(pins[0], HIGH);  
      digitalWrite(pins[1], LOW); 
      digitalWrite(pins[2], LOW); 
      digitalWrite(pins[3], HIGH); 
    break;  
    default: 
      digitalWrite(pins[0], LOW);  
      digitalWrite(pins[1], LOW); 
      digitalWrite(pins[2], LOW); 
      digitalWrite(pins[3], LOW); 
    break;  
  } 
}
bool motors[] = {false,false,false,false};
void loop() 
{ 
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    if (incomingByte == 'U') {
      motors[0] = true;
      motors[2] = false;
    }else if(incomingByte == 'D'){
      motors[0] = false;
      motors[2] = true;
    }else if(incomingByte == 'R'){
      motors[1] = true;
      motors[3] = false;
    }else if(incomingByte == 'L'){
      motors[1] = false;
      motors[3] = true;
    }
    Serial.write("D");
    for (int i=0; i<5; i++){
      driveStep(motors);
    }
    incomingByte = 0;
    
  }
  //for(int i=0; i<512; i++){
    //driveStep(motors);
  //}
 // motors[0] = !motors[0];
 // motors[1] = !motors[1];
  //motors[2] = !motors[2];
 // motors[3] = !motors[3];
 // delay(1000);
  
 
}
