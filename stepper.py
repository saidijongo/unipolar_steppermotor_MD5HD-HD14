import RPi.GPIO as GPIO
import time

# Defining pins
CW_PIN = 38   # CW+ pin
CCW_PIN = 36  # CCW+ pin
LEFT_SENSOR_PIN = 40  # Left photomicrosensor pin
RIGHT_SENSOR_PIN = 32 # Right photomicrosensor pin

# Define the delay for smooth rotation
DELAY = 0.009

# Set up the GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(CW_PIN, GPIO.OUT)
GPIO.setup(CCW_PIN, GPIO.OUT)
GPIO.setup(LEFT_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to rotate the motor 360 degrees
def rotate_360(direction_pin):
    for _ in range(500):  # 500 steps for 360 degrees
        GPIO.output(direction_pin, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(direction_pin, GPIO.LOW)
        time.sleep(DELAY)
       
def stop():
GPIO.output(CW_PIN, GPIO.LOW)
GPIO.output(CCW_PIN, GPIO.LOW)


try:
    while True:
        # when the right sensor is interrupted
        if GPIO.input(RIGHT_SENSOR_PIN) == GPIO.LOW:
            # 3 seconds Stop
            time.sleep(3)
            # counter-clockwise until the left sensor is interrupted
            while GPIO.input(LEFT_SENSOR_PIN) == GPIO.HIGH:
                print("Rotating counter clockwise")
                rotate_360(CCW_PIN)
               
        # when the left sensor is interrupted
        elif GPIO.input(LEFT_SENSOR_PIN) == GPIO.LOW:
            # Stop completely
            stop()
            break
        else:
            # Rotate clockwise
            print("Rotating clockwise")
            rotate_360(CW_PIN)

except KeyboardInterrupt:
    GPIO.cleanup()