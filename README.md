# MiniFRC Driver Station and Robot Code
Follow the tutorials [TODO: link tutorial]. You shouldn't need to download the source unless you want to play around with it.

NOTE: Do not use any blank lines in the config file.

Things you can type into the config file (exclude "<>"):
```
COM<#>      // defines the COM port number the program will try to connect to the robot with
joystick    // tells the program that you intend to use a joystick

// Sets up an axis controlled by 2 keyboard keys; ex: W and S
axis,<name>,<forward key>,<backward key>
// Sets up an axis controlled by a joystick, supports multiple joysticks
axis,<name>,<joystick number>,<joystick axis>

button,<name>,<key>                                       // Sets up a button controlled by the keyboard
button,<name>,<joystick number>,<joystick button number>  // Sets up a button controlled by a joystick button

// Changes the baudrate of the driver station from 9600 to whatever number you choose
BAUD,<number>

```
