import RPi.GPIO as GPIO
import time
import os



# setting up the GPIO mode to read off pin location rather than GPIO port number
#GPIO.setmode(GPIO.BOARD)

# setting up pin 11 as x-axis and pin 13 as y-axis
servoPinX = 11
servoPinY = 13 

# setting the GPIO ports as outputs
#GPIO.setup(servoPinX, GPIO.OUT)
#GPIO.setup(servoPinY, GPIO.OUT)

# 50Hz frequency for both servos
#pwmX = GPIO.PWM(servoPinX, 50)
#pwmY = GPIO.PWM(servoPinY, 50)

# start position of servos
#pwmX.start(0)
#pwmY.start(0)

def positionServo(servo, angle):
    os.system("python angleServoControl.py " + str(servo) + " " + str(angle))
    
# screen resolution: 1280x720
# center position: 640x360
# x axis range: 600 < x < 680
# y axis range: 330 < y < 390 
def servoPosition(x, y):
    global xAxisAngle
    global yAxisAngle
    
    
    if(x < 600):
        xAxisAngle += 10
        if xAxisAngle > 140:
            xAxisAngle = 140
        positionServo(servoPinX, xAxisAngle)
    if(x > 680):
        xAxisAngle -= 10
        if xAxisAngle < 40:
            xAxisAngle = 40
        positionServo(servoPinX, xAxisAngle)
    if(y < 330):
        yAxisAngle += 10
        if yAxisAngle > 140:
            yAxisAngle = 140
        positionServo(servoPinY, yAxisAngle)
    if(y > 390):
        yAxisAngle -= 10
        if yAxisAngle > 140:
            yAxisAngle = 140
        positionServo(servoPinY, yAxisAngle)

global xAxisAngle
xAxisAngle = 90
global yAxisAngle
yAxisAngle = 90

positionServo(servoPinX, xAxisAngle)
positionServo(servoPinY, yAxisAngle)


# stops x axis pwm
#pwmX.stop()
# stops y axis pwm
#pwmY.stop()

#GPIO.cleanup()
    
    
    
    
    