from gpiozero import AngularServo
from time import sleep

servo = AngularServo(17, min_angle=0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def set_angel(angel):
	servo.angle = angle
	sleep(1)
	
try:
	while True:
		angel = int(input("Enter angel (0 to 180): "))
		set_angle(angle)
except KeyboardInterrupt:
	print("Program stopped by user")

