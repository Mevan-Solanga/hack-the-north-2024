from gpiozero import AngularServo
from time import sleep

servo = AngularServo(17, min_angle=-90, max_angle=90)

while True:
    servo.angle = 75
    sleep(2)
    servo.angle = 45
    sleep(2)
