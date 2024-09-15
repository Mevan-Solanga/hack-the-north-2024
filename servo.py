class GPIOServo:

    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)  # Use BCM numbering
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(7.5) 
    
    # Function to move the servo to a specific angle
    def move_to_angle(degree):
        # Constrain the degree value between 0 and 180
        if degree < 0:
            degree = 0
        elif degree > 180:
            degree = 180
        
        # Convert the angle to duty cycle
        duty = (degree / 18.0) + 2.5  # Map 0-180 degrees to duty cycle 2.5-12.5
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)  # Give enough time for the servo to reach the position
        self.pwm.ChangeDutyCycle(0)

    def change_state(self, is_up = False):
        if is_up:
            move_to_angle(20)
        else:
            move_to_angle(0)

    def __del__(self):
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()
        GPIO.cleanup()