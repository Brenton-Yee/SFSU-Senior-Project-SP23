from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarning(False)

def setServoAngle(servo, angle):
    pwm = GPIO.PWM(servo, 50)
    pwm.start(0)
    dutyCycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.3)
    pwm.stop()
    
    
if __name__ == '__main__':
    import sys
    servo = int(sys.argv[1])
    GPIO.setup(servo, GPIO.OUT)
    setServoAngle(servo, int(sys.argv[2]))
    GPIO.cleanup()

    