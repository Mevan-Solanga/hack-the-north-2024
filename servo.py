from gpiozero import Servo
from time import sleep
from gpiozero import AngularServo
#from gpiozero.pins.pigpio import PiGPIOFactory
#from gpiozero import Device

#Device.pin_factory = PiGPIOFactory()

servo = AngularServo(17)

while True:
    servo.angle = -20
    sleep(2)
    servo.angle = 40
    sleep(2)
