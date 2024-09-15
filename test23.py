import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the servo
SERVO_PIN = 23

# Set up the GPIO pin as an output
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set up PWM with a frequency of 50 Hz (common for servos)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)  # Start PWM with 0 duty cycle

def set_angle(angle):
    # Calculate the duty cycle for the desired angle
    # Typically, the duty cycle for 0 degrees is around 2.5%, and for 180 degrees it's around 12.5%
    duty_cycle = -(angle / 18) + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Allow time for the servo to reach the position

try:
    set_angle(20)
    set_angle(0)
    
finally:
    # Ensure proper cleanup
    try:
        pwm.stop()
    except Exception as e:
        print(f"Failed to stop PWM: {e}")
    GPIO.cleanup()
