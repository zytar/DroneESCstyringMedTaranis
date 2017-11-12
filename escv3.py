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

#interval = 0.1
jesus = 0

#######################################################################

print "Ready to ARM!"

def controller(jesus,inp):
#	print "PLEASE ENSURE THAT PROPELLERS ARE DETACHED, BECAUSE THE ENGINES WILL SPIN IN 5 SECONDS!"
	time.sleep(0.05)
#	print "Control speed with joystick"
	pygame.init()

	if jesus<3:
		print ""
		inp2 = raw_input
	else:
		inp2 = ""
	jesus = 5

        my_joystick = pygame.joystick.Joystick(0)
        my_joystick.init()
        clock = pygame.time.Clock()

	boo = False
	while True:

                for event in pygame.event.get():
                        print "y1= " , ((my_joystick.get_axis(2) + 1)/2), my_joystick.get_button(1)
                        clock.tick(1000)

		y1 = (my_joystick.get_axis(2) + 1)/2
		inp2 = my_joystick.get_button(1)

		print inp2

		if y1 != 0.5:
			boo = True

		print y1

		if boo:
			speed = 750+y1*1300
		else:
			speed = 750

		pi.set_servo_pulsewidth(ESC1, speed)
        	pi.set_servo_pulsewidth(ESC2, speed)
       		pi.set_servo_pulsewidth(ESC3, speed)
        	pi.set_servo_pulsewidth(ESC4, speed)

		if inp2 > 0.6:
	        	print "-----ARMED-----"
			controller(jesus, inp)
			break
		elif inp2 < 0.4:
		    	print "-----DISARMED-----"
			stop()
			break
#		elif inp == "no":
#		    stop()
#		    break
	        else:
       		    print ""

#####################################################################

def arm(jesus, inp): #This is the arming procedure of an ESC
#	print "Vi er er ARM!"
	if inp > 0.6:
		print "Arming the drone"
		time.sleep(1)
		pi.set_servo_pulsewidth(ESC1, 0)
	        pi.set_servo_pulsewidth(ESC2, 0)
	        pi.set_servo_pulsewidth(ESC3, 0)
	        pi.set_servo_pulsewidth(ESC4, 0)
	        time.sleep(1)
		pi.set_servo_pulsewidth(ESC1, max_value)
	        pi.set_servo_pulsewidth(ESC2, max_value)
	        pi.set_servo_pulsewidth(ESC3, max_value)
	        pi.set_servo_pulsewidth(ESC4, max_value)
	        time.sleep(1)
		pi.set_servo_pulsewidth(ESC1, min_value)
	        pi.set_servo_pulsewidth(ESC2, min_value)
	        pi.set_servo_pulsewidth(ESC3, min_value)
	       	pi.set_servo_pulsewidth(ESC4, min_value)
	        controller(jesus,inp)

#######################################################################

def armsjekk(jesus, inp): #This will stop every action your Pi is performing for ESC ofcourse.
	if inp < 0.4:
		time.sleep(0.5)
		print "Drona er disarmert"
		stop(inp)
	elif inp > 0.6:
#		print "Armerer dronen, propeller vil starte om 5 sekunder"
#		time.sleep(5)
		arm(jesus,inp)

#######################################################################

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
#	print "The drone is disarmed. Press button to arm!"
	while True:
		for events in pygame.event.get():
			print "", my_joystick.get_button(1)
			clock.tick(1000)

		inp = my_joystick.get_button(1)

		if inp < 0.4:
			time.sleep(1)
			pi.set_servo_pulsewidth(ESC1, 0)
			pi.set_servo_pulsewidth(ESC2, 0)
			pi.set_servo_pulsewidth(ESC3, 0)
			pi.set_servo_pulsewidth(ESC4, 0)
			stop()
		else:
			armsjekk(jesus,inp)
#######################################################################

def calibrate():
    pi.set_servo_pulsewidth(ESC1, 0)
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.set_servo_pulsewidth(ESC3, 0)
    pi.set_servo_pulsewidth(ESC4, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC1, max_value)
	pi.set_servo_pulsewidth(ESC2, max_value)
	pi.set_servo_pulsewidth(ESC3, max_value)
	pi.set_servo_pulsewidth(ESC4, max_value)

        print"Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter"
        inp = raw_input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC1, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            pi.set_servo_pulsewidth(ESC3, min_value)
            pi.set_servo_pulsewidth(ESC4, min_value)

            print "Wierd eh! Special tone"
            time.sleep(7)
            print "Wait for it ...."
            time.sleep (5)
            print "Im working on it, DONT WORRY JUST WAIT....."
            pi.set_servo_pulsewidth(ESC1, 0)
            pi.set_servo_pulsewidth(ESC2, 0)
            pi.set_servo_pulsewidth(ESC3, 0)
            pi.set_servo_pulsewidth(ESC4, 0)
            time.sleep(2)
            print "Arming ESC now..."
            pi.set_servo_pulsewidth(ESC1, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            pi.set_servo_pulsewidth(ESC3, min_value)
            pi.set_servo_pulsewidth(ESC4, min_value)
            time.sleep(1)
            print "See.... uhhhhh"
            stop()

######################################################################



inp = my_joystick.get_button(1)
#inp3 = raw_input()

if inp > 0.6 :
	arm(jesus)
elif inp < 0.4 :
	stop()
#elif inp3 == "calibrate":
#	calibrate()
elif inp == "no":
    print "Farewell then!"
    stop()

else:
	print "Whops, something went wrong, please restart the program" 

