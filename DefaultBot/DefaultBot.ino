#include <SoftwareSerial.h>
#include <AFMotor.h>

/* <==============================================================>
 *  You will need to change the following variables depending on what
 *  analog pins on your motor shield you are using, which motor goes to
 *  which port, and if your drive logic is flipped. */

SoftwareSerial bluetooth(A0, A1); //RX,TX

/* These lines declare the motors and which ports they will be connected to on the motor shield.
 *  For each side, connect both motors to the shield on the same port.
 *  This leaves the other two ports open for motors with other functions. */
AF_DCMotor motorL(2);
AF_DCMotor motorR(3);

/* You may want to add more motors, like a climber motor.
 *  To do that, uncomment the following line of code and hook up your motor to port 4.
 *  If you are adding another motor you will need to follow more instructions further down. */
// AF_DCMotor climber(4);

int xAxisMultiplier = 1;      // Change this variable to -1 if your robot turns the wrong way
int yAxisMultiplier = 1;       // Change ths variable to -1 if your robot drives backward when it should be going forward

/* You shouldn't need to change anything past here unless you're adding
 *  something like an automode or an extra motor. 
 *  <==============================================================> */

// Variables used to recive data from the driverstation and calculate drive logic
float xAxis, yAxis;
int velocityL, velocityR;

// Add this line of code if you're adding a button for a climber or some other system
//float button;

// In setup, we tell bluetooth communication to start and set all of our motors to not move
void setup() {
  bluetooth.begin(9600);
  drive(0, 0);
}

void loop() {
  while(bluetooth.available() > 0){                                   // This line checks for any new data in the buffer from the driverstation
    if ((bluetooth.read()) == 'z'){                                   // We use 'z' as a delimiter to ensure that the data doesn't desync
      xAxis = (bluetooth.parseFloat()) * (100) * xAxisMultiplier;     // For each axis the driver station sends, we have a variable here to recieve it
      yAxis = (bluetooth.parseFloat()) * (100) * yAxisMultiplier;     

/* If you're adding a  motor, add this. Also remember to initialize the climber motor port,
 *  define the variable to hold the button state, and add the button in your config file. */

/*
      button = bluetooth.parseFloat();      
            
      if (button == 1){
        climber.run(FORWARD);
        climber.setSpeed(255);
      } else {
        climber.run(FORWARD);
        climber.setSpeed(0);
      }
*/
      
      // This line tells the drive function what speed and direction to move the motors in
      drive(xAxis, yAxis);
    } 
  }
}

// This function handles drive logic and actuation. Don't change this unless you know what you're doing.
void drive(int xAxis, int yAxis) {
  float V = (100 - abs(xAxis)) * (yAxis/100) + yAxis;    // This is where the X and Y axis inputs are converted into tank drive logic
  float W = (100 - abs(yAxis)) * (xAxis/100) + xAxis;
  velocityL = ((((V-W)/2)/100)*255);
  velocityR = ((((V+W)/2)/100)*255);

  motorR.run((velocityR >= 0) ? FORWARD : BACKWARD);     // These comands tell the motors what speed and direction to move at
  motorR.setSpeed(abs(velocityR));
  motorL.run((velocityL >= 0) ? FORWARD : BACKWARD);
  motorL.setSpeed(abs(velocityL));
}

