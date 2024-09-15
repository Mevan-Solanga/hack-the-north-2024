import time
import RPi.GPIO as GPIO

pin = 25  # Use pin 17 for BCM numbering

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(pin, GPIO.OUT)

# Initialize PWM with 50 Hz frequency
pwm = GPIO.PWM(pin, 50)
pwm.start(7.5)  # Start with the servo in the center position (90 degrees)

# Function to move the servo to a specific angle
def move_to_angle(degree):
    # Constrain the degree value between 0 and 180
    if degree < 0:
        degree = 0
    elif degree > 180:
        degree = 180
    
    # Convert the angle to duty cycle
    duty = (degree / 18.0) + 2.5  # Map 0-180 degrees to duty cycle 2.5-12.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Give enough time for the servo to reach the position
    pwm.ChangeDutyCycle(0)  # Stop PWM signal after movement

# Move the servo to left 90 degrees with intermediate steps
def smooth_left_90():
    print("Moving to left 90 degrees")
    move_to_angle(45)  # Intermediate position to smooth the transition
    time.sleep(0.3)    # Small pause to let the servo settle
    move_to_angle(0)   # Final move to 0 degrees (left)
    time.sleep(0.5)

# Move the servo to right 90 degrees
def right_90():
    print("Moving to right 90 degrees")
    move_to_angle(180)  # 180 degrees represents the far right

# Move the servo back to center
def center():
    print("Returning to center (90 degrees)")
    move_to_angle(90)  # 90 degrees is the center

# Function to stop the PWM and clean up GPIO
def stop():
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()
    print("Servo stopped and GPIO cleaned up")

# Move servo to the left, right, and then back to center
try:
    smooth_left_90()  # Smooth move to 0 degrees (left)
    time.sleep(1)     # Wait for 1 second
    right_90()        # Move to 180 degrees (right)
    time.sleep(1)     # Wait for 1 second
    center()          # Move back to 90 degrees (center)
    time.sleep(1)     # Wait for 1 second
    smooth_left_90()  # Smooth move to 0 degrees (left)
    time.sleep(1)     # Wait for 1 second
    right_90()        # Move to 180 degrees (right)
    time.sleep(1)     # Wait for 1 second
    center()          # Move back to 90 degrees (center)
    time.sleep(1)     # Wait for 1 second
    smooth_left_90()  # Smooth move to 0 degrees (left)
    time.sleep(1)     # Wait for 1 second
    right_90()        # Move to 180 degrees (right)
    time.sleep(1)     # Wait for 1 second
    center()          # Move back to 90 degrees (center)
    time.sleep(1)     # Wait for 1 second

finally:
    stop()  # Ensure the servo is stopped and GPIO is cleaned up
