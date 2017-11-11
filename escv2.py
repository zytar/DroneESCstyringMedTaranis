import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import pygame
pygame.init()
print "Joystics: ", pygame.joystick.get_count()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock = pygame.time.Clock()

#ESC's in these GPIO pins
ESC1=4
ESC2=17
ESC3=27
ESC4=22

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
pi.set_servo_pulsewidth(ESC4, 0)

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 700  #change this if your ESC's min value is different or leave it be

throttle1 = ESC1
throttle2 = ESC2
throttle3 = ESC3
throttle4 = ESC4
interval = 0.1

#y1 = my_joystick.get_axis(3)

#######################################################################

print "Do you want to arm the motors? (yes or no)"

def yes(my_joystick):
	print "PLEASE ENSURE THAT PROPELLERS ARE DETACHED, BECAUSE THE ENGINES WILL SPIN IN 5 SECONDS!"
	time.sleep(5)
	print "Control speed with joystick"
	pygame.init()
	my_joystick.init()
	y1 = my_joystick.get_axis(3)
	speed = 700+y1*1300
	while True:
		pi.set_servo_pulsewidth(ESC1, speed)
        	pi.set_servo_pulsewidth(ESC2, speed)
       		pi.set_servo_pulsewidth(ESC3, speed)
        	pi.set_servo_pulsewidth(ESC4, speed)
        	inp = raw_input()

		if inp == "yes":
	            arm(my_joystick)
		    break
		elif inp == "stop":
		    stop()
		    break
		elif inp == "no":
		    stop()
		    break

	        else:
       		    print "Whoops, wrong button!"

#####################################################################

def arm(my_joystick): #This is the arming procedure of an ESC
	print "Connect the battery and press Enter. Props should be detached!"
	inp = raw_input()
	if inp == '':
		pi.set_servo_pulsewidth(ESC1, 0)
	        pi.set_servo_pulsewidth(ESC2, 0)
	        pi.set_servo_pulsewidth(ESC3, 0)
	        pi.set_servo_pulsewidth(ESC4, 0)
	        pi.set_servo_pulsewidth(ESC1, max_value)
	        pi.set_servo_pulsewidth(ESC2, max_value)
	        pi.set_servo_pulsewidth(ESC3, max_value)
	        pi.set_servo_pulsewidth(ESC4, max_value)
	        pi.set_servo_pulsewidth(ESC1, min_value)
	        pi.set_servo_pulsewidth(ESC2, min_value)
	        pi.set_servo_pulsewidth(ESC3, min_value)
	       	pi.set_servo_pulsewidth(ESC4, min_value)
	        yes(my_joystick)

#######################################################################

def controller():
	pygame.init()
	my_joystick = pygame.joystick.Joystick(0)
	my_joystick.init()
	clock = pygame.time.Clock()
	while 1:
		for event in pygame.event.get():
                        print "y1= " , my_joystick.get_axis(3)
                        clock.tick(1000)
		pygame.quit()
		arm(my_joystick)

#######################################################################

def no(): #This will stop every action your Pi is performing for ESC ofcourse.
	pi.set_servo_pulsewidth(ESC1, 0)
	pi.set_servo_pulsewidth(ESC2, 0)
	pi.set_servo_pulsewidth(ESC3, 0)
	pi.set_servo_pulsewidth(ESC4, 0)
	pi.stop()

#######################################################################

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC1, 0)
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.set_servo_pulsewidth(ESC3, 0)
    pi.set_servo_pulsewidth(ESC4, 0)
    pi.stop()

#######################################################################

inp = raw_input()

if inp == "yes":
    controller()

elif inp == "stop":
    stop()

elif inp == "no":
    print "Farewell then!"
    stop()
else:
    print "Whops, something went wrong, please restart the program"
