'''
MiniFRC driver station 2017
By Squidfairy/Goosefairy/ddthj/michael/Terrorbytes/FRC4561/a couple goblins/you get the idea

TODO:

[x] test
[] add numbers as keyboad buttons support (will require a "#" infront of the number in the config file)
[] add ability to scroll through log (something to do with pygame.mouseup and mousedown?)
[] add visuals to inputs kinda like the microsoft joystick tester thing
[] test more
[] debug till infinity
[] finish this list
'''
version = 3.4

import pygame
import time
import serial

pygame.init()

display = pygame.display.set_mode((1000,800))

Text = pygame.font.SysFont("courier",20)
white = (240,240,240)
black = (0,0,0)
display.fill(white)
pygame.display.update()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class print_():
    def __init__(self):
        self.stack = []
        self.log = 0
    def P(self,text):
        print(str(text))
        if text[0] == '/':
            self.stack.append(" ")
            text = text[1:]
        self.stack.append(str(text))
        if len(self.stack) > 20:
            self.log += 1
        self.render()
        pygame.display.update()
        
        
    def render(self):
        for i in range(0,len(self.stack)-1):
            b = str(self.stack[i])
            a = (24 * i) - (self.log * 24)
            if a >=0:
                rendertext(20,b,10,int(a))

def rendertext(scale,text,x,y):
    font = pygame.font.SysFont("courier",scale)
    thing = font.render(text,1,black)
    display.blit(thing,(x,y))
    
class axis():
    def __init__(self,name,a,b):
        self.name = name
        if a.isdigit():
            self.joystick = True
            self.joystick_num = int(a)
            self.joystick_axis = int(b)
            p.P('[INFO] Added "%s" joystick-controlled axis to package list' % (self.name))
        else:
            self.joystick = False
            self.forward = int(alphabet.index(a) + 97)
            self.backward = int(alphabet.index(b) + 97)
            p.P('[INFO] Added "%s" keyboard-controlled axis to package list' % (self.name))
            
    def tick(self,events,joysticks):
        if self.joystick == True:
            return str(round(joysticks[self.joystick_num].get_axis(self.joystick_axis),1))
        else:
            if events[self.forward] == True:
                return "1"
            elif events[self.backward] == True:
                return "-1"
            else:
                return "0"

class button():
    def __init__(self,name,a,b = 0):
        self.name = name
        if a.isdigit():
            self.joystick = True
            self.joystick_num = int(a)
            self.joystick_button = int(b)
            p.P('[INFO] Added "%s" joystick-controlled button to package list' % (self.name))
        else:
            self.joystick = False
            self.key = int(alphabet.index(a) + 97)
            p.P('[INFO] Added "%s" keyboard-controlled button to package list' % (self.name))
            
    def tick(self,events,joysticks):
        if self.joystick == True:
            return str(joysticks[self.joystick_num].get_button(self.joystick_button))
        else:
            if events[self.key] == True:
                return "1"
            else:
                return "0"

def connect(default,num = -1):
    if num == -1:
        try:
            s = serial.Serial(str(default),9600,timeout = 1)
            return s
        except:
            p.P("[WARNING] Couldn't connect to robot with specified COM port in config file")
            return None
            
            #num+=1
            #connect(default,num)
        #this is all the autosearch stuff that is kinda sketchy, only use if nothing else is connected to computer maybe?
    else:
        try:
            com = "COM" + str(num)
            s = serial.Serial(str(com),9600,timeout = 1)
            return s
        except:
            p.P("[DEBUG] Couldn't connect to robot on %s" % (str(com)))
            if num < 50:
                num+=1
                connect(default,num)
            else:
                p.P("[WARNING] Couldn't connect to robot on ANY port!")
                return None
            
flag = False
p = print_()
com = ""
package = []    
p.P("MiniFRC Driver Station 2017 V%s"%(str(version)))
p.P("Booting...")
joystick_mode = False
try:
    f = open("config.txt","r")
    p.P("[INFO] found config.txt, reading...")
    #to create a new axis
    
    #axis,name,key_forward,key_backward
    #axis,name,joystick_number,joystick_axis_number

    #to create a new button
    
    #button,name,key
    #button,name,joystick_number,joystick_button_number
    try:
        for line in f:
            if line.find("axis") != -1:
                v = line.split(",")
                package.append(axis(v[1],v[2],v[3]))
            elif line.find("button") != -1:
                v = line.split(",")
                print(len(v))
                if len(v) < 4:
                    package.append(button(v[1],v[2]))
                else:
                    package.append(button(v[1],v[2],v[3]))
            elif line.find("joystick") != -1:
                joystick_mode = True
            elif line.find("COM")!= -1:
                com = line.strip('\n')
                

        if joystick_mode:
            p.P("[INFO] Joysticks enabled in config file, loading joystick control")
            pygame.joystick.init()
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            p.P("/Detected %s joystick(s): " % (pygame.joystick.get_count())+str(joysticks))
            if pygame.joystick.get_count() > 0:
                for i in range(pygame.joystick.get_count()):
                    joystick = pygame.joystick.Joystick(i)
                    joystick.init()
                    for i in range(0,5):
                        events = pygame.event.get()
                        time.sleep(0.1)
                    name = joystick.get_name()
                    p.P("/Joystick name: %s" % (name))
                    
                    axes = joystick.get_numaxes()
                    p.P("Num of axes: %s" % (axes))
                    
                    for j in range( axes ):
                        axis = joystick.get_axis( j )
                        p.P("Axis %s value: %s" % (j, axis) )
                        
                    buttons = joystick.get_numbuttons()
                    p.P("Number of buttons: %s"%(buttons))

                    for k in range( buttons ):
                        button = joystick.get_button( k )
                        p.P("Button %s value: %s"%(k,button))

                    hats = joystick.get_numhats()
                    p.P("Number of hats: %s" % (hats))
                    
                    for l in range( hats ):
                        hat = joystick.get_hat( l )
                        p.P("Hat %s value: %s" % (l, hat))
            else:
                p.P("[WARNING] Joysticks enabled in config file but no joysticks found! Shutting Down!")
                flag = True
        else:
            p.P("[INFO] Joysticks not enabled in config file, not loading joystick control")
    except Exception as e:
        p.P('[WARNING] Improperly formatted config file or lazy programming led to this error')
        flag = True
except:
    p.P('[WARNING] Could not find/open "config.txt"')
    flag = True

s = connect(com)
joysticks = []
if s != None and flag == False:
    p.P("[INFO] Connected to robot!")

    if joystick_mode == True and int(pygame.joystick.get_count()) > 0:
        joystick_one = pygame.joystick.Joystick(0)
        joysticks.append(joystick_one)
        if pygame.joystick.get_count() > 1:
            joystick_two = pygame.joystick.Joystick(1)
            joysticks.append(joystick_two)    
    Clock = pygame.time.Clock()
    while 1:
        display.fill(white)
        pak = ""
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
                
        for item in package:
            pak += str(item.tick(keys,joysticks)) + ";"
        p.P(str(pak)) # this will probably get changed so that the current input stays in one place onscreen
        s.write(bytes(pak,'utf-8'))
        p.render()
        pygame.display.update()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        Clock.tick(20)
