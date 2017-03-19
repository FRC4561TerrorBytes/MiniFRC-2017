# MiniFRC-2017
Driver Station source for MiniFRC 2017

Follow the tutorials, you shouldn't need to download the source unless you want to play around with it


NOTE: do not use any blank lines in the config file, in theory the code ignores them but in practice there's a bug somewhere

Things you can type into the config file (exclude all carrots <>):
```
COM<#>      <defines the COM port number the program will try to connect to the robot with
joystick    <tells the program that you intend to use a joystick

axis,<name>,<forward key>,<backward key>        <sets up an axis controlled by 2 keyboard keys; ex: w and s
axis,<name>,<joystick number>,<joystick axis>   <sets up an axis controlled by a joystick, supports multiple joysticks

button,<name>,<key>                              <sets up a button controlled by the keyboard
button,<name>,<joystick number>,<joystick button number>  <sets up a button controlled by a joystick button
```
