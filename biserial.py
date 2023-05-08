#!/usr/bin/env python3
import serial
import time

class Controller:
    
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
        time.sleep(1)
        self.ser.reset_input_buffer()
        self.xAxisAngle = 80
        self.yAxisAngle = 98
        
    def map_range(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    def servo_pos(self, x, y):
#         if not self.ser.is_open:
#                 self.ser.open()
        if(x < 600):
            self.xAxisAngle += 10
            if self.xAxisAngle > 110:
                self.xAxisAngle = 110
            self.ser.write(bytes(str(self.map_range(self.xAxisAngle, 40, 110, 2, 255)), 'ascii'))
#             self.ser.close()
        elif(x > 680):
            self.xAxisAngle -= 10
            if self.xAxisAngle < 30:
                self.xAxisAngle = 30
            self.ser.write(bytes(str(self.map_range(self.xAxisAngle, 40, 110, 2, 255)), 'ascii'))
#             self.ser.close()
#         if not self.ser.is_open:
#                 self.ser.open()
#         if(y < 330):
#             self.yAxisAngle += 10
#             if self.yAxisAngle > 115:
#                 self.yAxisAngle = 115
#             self.ser.write(bytes(str(self.map_range(self.yAxisAngle, 105, 115, 129, 255)), 'ascii'))
# #             self.ser.close()
#         elif(y > 390):
#             self.yAxisAngle -= 10
#             if self.yAxisAngle < 105:
#                 self.yAxisAngle = 105
#             self.ser.write(bytes(str(self.map_range(self.yAxisAngle, 105, 115, 129, 255)), 'ascii'))
#             self.ser.close()
        return

    def light(self, yes):
#         if not self.ser.is_open:
#                 self.ser.open()
        if yes:
            self.ser.write(bytes(str(1), 'ascii'))
            print('light')
        else:
            self.ser.write(bytes(str(0), 'ascii'))
            print('dark')
#         self.ser.close()
        return

if __name__ == '__main__':
    
    Test = Controller()
    
    while True:
        inst = input("Enter instruction: ")
        if(inst.isdigit()):
            number = int(inst)
        else:
            number = -1

        if number >= 0 and number <= 255:
            print("Sending number " + str(number) + " to Arduino.")
            Test.ser.write(bytes(str(number), 'ascii'))
#             print(ser.readline().decode('utf-8').rstrip())

            