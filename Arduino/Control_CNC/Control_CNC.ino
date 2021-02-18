/////////////////////////
// Autor: Debora Lopez
////////////////////////

int en_mot = 12; //Enable motors
// Step de los motores
int step_y = 4;
int step_x = 3;
int step_z = 2;
// Direccion de los motores
int dir_y = 7;
int dir_x = 6;
int dir_z = 5;
//Controles 
int y_up = 0;
int y_down = 0;
int x_up = 0;
int x_down = 0;
int z_up = 0;
int z_down = 0;

int speed_in = A0;


////////////////////////////////////////////////////////////////////////////////////
float turns_per_cm = 3.5;             //Esta es la cantidad de vueltas que necesita el tornillo guía para dar una vuelta
float steps_per_revolution = 200;   //Esta es la cantidad de pasos que necesita el motor para una rotación completa
float max_speed = 17;               //Velocidad en mm por segundo
float min_speed = 0.6;              //Velocidad en mm por segundo
////////////////////////////////////////////////////////////////////////////////////




/////
float mm_per_step = 0.007142;     //El valor inicial aumenta de 7 vueltas por cm y 200 pasos por rotación completa
float pos_y = 0;
float pos_x = 0;
float pos_z = 0;
float DELAY = 0;
float RealSpeed = 0;
unsigned long previousMillis = 0; 
bool step_y_status = false;
bool step_x_status = false;
bool step_z_status = false;
float max_delay = 0;
float min_delay = 0;



void setup() {  
  Serial.begin(9600); //Comunicacion serial
  //Define the pins as inputs or outputs
  pinMode(en_mot,INPUT);
  pinMode(x_up,INPUT);
  pinMode(x_down,INPUT);
  pinMode(y_up,INPUT);
  pinMode(y_down,INPUT);
  pinMode(speed_in,INPUT); 
  ///outputs
  pinMode(step_y,OUTPUT);  
  pinMode(step_x,OUTPUT);
  pinMode(step_z,OUTPUT);
  pinMode(dir_y,OUTPUT);
  pinMode(dir_x,OUTPUT);
  pinMode(dir_z,OUTPUT);  
  //Calculate the delay for the speed control
  mm_per_step = (10/turns_per_cm)/steps_per_revolution;
  max_delay = min_speed*20000;
  min_delay = max_speed*23;
}

void loop() {
  //Read the analog input of A0 and create the speed delay
  int analog_in = analogRead(speed_in);
  DELAY = map(analog_in,0,1024,max_delay, min_delay);    
  RealSpeed = (1000000/DELAY)*mm_per_step;

  //Move X up
  if(digitalRead(x_up) && !digitalRead(x_down) && !digitalRead(y_up) && !digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_x_status = !step_x_status;
    digitalWrite(dir_x,HIGH);   //CW
    digitalWrite(step_x,step_x_status);
    delayMicroseconds(DELAY); 
    pos_x = pos_x + mm_per_step;  
  }

  //Move X down
   if(!digitalRead(x_up) && digitalRead(x_down) && !digitalRead(y_up) && !digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_x_status = !step_x_status;
    digitalWrite(dir_x,LOW);   //CCW
    digitalWrite(step_x,step_x_status);
    delayMicroseconds(DELAY);    
    pos_x = pos_x - mm_per_step;
    
  }

  //Move Y up
  if(!digitalRead(x_up) && !digitalRead(x_down) && digitalRead(y_up) && !digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_y_status = !step_y_status;
    digitalWrite(dir_y,HIGH);   //CW
    digitalWrite(step_y,step_y_status);
    delayMicroseconds(DELAY);   
    pos_y = pos_y + mm_per_step;
    
  }

  //Move Y down
  if(!digitalRead(x_up) && !digitalRead(x_down) && !digitalRead(y_up) && digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_y_status = !step_y_status;
    digitalWrite(dir_y,LOW);   //CCW
    digitalWrite(step_y,step_y_status);
    delayMicroseconds(DELAY);  
    pos_y = pos_y - mm_per_step;
    
  }

  

  //Move X up and Y up
  if(digitalRead(x_up) && !digitalRead(x_down) && digitalRead(y_up) && !digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_x_status = !step_x_status;
    step_y_status = !step_y_status;
    digitalWrite(dir_x,HIGH);   //CW
    digitalWrite(dir_y,HIGH);   //CW
    digitalWrite(step_x,step_x_status);
    digitalWrite(step_y,step_y_status);
    delayMicroseconds(DELAY);    
    pos_x = pos_x + mm_per_step;    
    pos_y = pos_y + mm_per_step;  
  }

  //Move X up and Y down
  if(digitalRead(x_up) && !digitalRead(x_down) && !digitalRead(y_up) && digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_x_status = !step_x_status;
    step_y_status = !step_y_status;
    digitalWrite(dir_x,HIGH);   //CW
    digitalWrite(dir_y,LOW);   //CCW
    digitalWrite(step_x,step_x_status);
    digitalWrite(step_y,step_x_status);
    delayMicroseconds(DELAY);
    pos_x = pos_x + mm_per_step;    
    pos_y = pos_y - mm_per_step;  
  }

  //Move X down and Y down
  if(!digitalRead(x_up) && digitalRead(x_down) && !digitalRead(y_up) && digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_x_status = !step_x_status;
    step_y_status = !step_y_status;
    digitalWrite(dir_x,LOW);   //CCW
    digitalWrite(dir_y,LOW);   //CCW
    digitalWrite(step_x,step_x_status);
    digitalWrite(step_y,step_y_status);
    delayMicroseconds(DELAY);
    pos_x = pos_x - mm_per_step;    
    pos_y = pos_y - mm_per_step;  
  }

  //Move X down and Y up
   if(!digitalRead(x_up) && digitalRead(x_down) && digitalRead(y_up) && !digitalRead(y_down) && !digitalRead(en_mot))
  {
    step_x_status = !step_x_status;
    step_y_status = !step_y_status;
    digitalWrite(dir_x,LOW);    //CCW
    digitalWrite(dir_y,HIGH);   //CW
    digitalWrite(step_x,step_x_status);
    digitalWrite(step_y,step_y_status);    
    delayMicroseconds(DELAY);
    pos_x = pos_x - mm_per_step;    
    pos_y = pos_y - mm_per_step;  
  }
}
