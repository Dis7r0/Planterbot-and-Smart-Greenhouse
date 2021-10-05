import RPi.GPIO as GPIO
import pygame
import time
import sys
import serial

try:
    ser = serial.Serial('/dev/ttyACM0',9600)
except:
    ser = serial.Serial('/dev/ttyACM1',9600)

s = [0]
'''
pygame.init()
pygame.joystick.init()

print(pygame.joystick.get_count())
_joystick = pygame.joystick.Joystick(0)
_joystick.init()
+*
clock = pygame.time.Clock()
'''

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

class Motors():
    def __init__(self,En1,En2,In1,In2,In3,In4):
        self.En1 = En1
        self.En2 = En2
        self.In1 = In1
        self.In2 = In2
        self.In3 = In3
        self.In4 = In4
        GPIO.setup(self.En1,GPIO.OUT)
        GPIO.setup(self.En2,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        GPIO.setup(self.In3,GPIO.OUT)
        GPIO.setup(self.In4,GPIO.OUT)
        self.pwm1 = GPIO.PWM(self.En1,1000)
        self.pwm2 = GPIO.PWM(self.En2,1000)
        self.pwm1.start(0)
        self.pwm2.start(0)
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(0)
    
    def moveF(self,x=100):
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        GPIO.output(self.In3,GPIO.LOW)
        GPIO.output(self.In4,GPIO.HIGH)
        self.pwm1.ChangeDutyCycle(x)
        self.pwm2.ChangeDutyCycle(x)
        
    def moveB(self,x=100):
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        GPIO.output(self.In3,GPIO.HIGH)
        GPIO.output(self.In4,GPIO.LOW)
        self.pwm1.ChangeDutyCycle(x)
        self.pwm2.ChangeDutyCycle(x)
    
    def moveR(self):
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        GPIO.output(self.In3,GPIO.LOW)
        GPIO.output(self.In4,GPIO.HIGH)
        self.pwm2.ChangeDutyCycle(100)
        self.pwm1.ChangeDutyCycle(100)
        
    def moveL(self):
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        GPIO.output(self.In3,GPIO.HIGH)
        GPIO.output(self.In4,GPIO.LOW)
        self.pwm1.ChangeDutyCycle(100)
        self.pwm2.ChangeDutyCycle(100)
    
    def stop(self):
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(0)
        

motor2 = Motors(2,5,3,4,26,6)
motor1 = Motors(25,17,23,24,22,27)
# motor2 = Motor(17,22,27)
# En,In1,In2 = 2,3,4
# GPIO.setup(En,GPIO.OUT)
# GPIO.setup(In1,GPIO.OUT)
# GPIO.setup(In2,GPIO.OUT)
# pwm = GPIO.PWM(En,100)
#pwm.start(0)
try:
    flag = 
0    turned = False
    forward_after_turned = False
    final_turn = False
    motor1.moveF(100)
    motor2.moveF(100)
    while flag == 0:
        read_serial=ser.readline()
        try:
            s[0] = str(int (ser.readline(),10))
        except:
            s[0] = str(int (ser.readline(),16))
        print(s[0])

        seconds = 0
        if(int(s[0])<500): #490
            # print("Turning")
            start_time = time.time()
            while seconds <= 3.25:
                # print("First turn")
                turned = True
                # print(seconds)
                motor1.moveR()
                motor2.moveR()
                end_time = time.time()
                seconds = end_time - start_time
                read_serial=ser.readline()
                try:
                    s[0] = str(int (ser.readline(),10))
                except:
                    s[0] = str(int (ser.readline(),16))
        # seconds_forward = 0
        # motor1.stop()
        # motor2.stop()
        seconds_forward = 0
        # print("Done turning")
        if(turned == True):
            start_time = time.time()
            # print("In front after turn")
            while seconds_forward <= 0.75:
                # print("Front in turn")
                # turned = True
                # print(seconds)
                motor1.moveF(100)
                motor2.moveF(100)
                end_time = time.time()
                seconds_forward = end_time - start_time
                read_serial=ser.readline()
                try:
                    s[0] = str(int (ser.readline(),10))
                except:
                    s[0] = str(int (ser.readline(),16))
                forward_after_turned = True
        # seconds_turn2 = 0
        # motor1.stop()
        # motor2.stop()
        seconds_turn2 = 0
        if(forward_after_turned == True):
            start_time = time.time()
            while seconds_turn2 <= 3.15:
                # print("Turn after front")
                # turned = True
                # print(seconds)
                print(motor1.moveR())
                print(motor2.moveR())
                end_time = time.time()
                seconds_turn2 = end_time - start_time
                read_serial=ser.readline()
                try:
                    s[0] = str(int (ser.readline(),10))
                except:
                    s[0] = str(int (ser.readline(),16))
                final_turn = True
                # print("Final turn {}".format(final_turn))
        # print("Final Turn: ")
        # print(final_turn)
        '''
        if seconds >= 5.2 and seconds2 >= 2:
            motor1.moveF(70)
            motor2.moveF(70)
        '''
        
        read_serial=ser.readline()
        try:
            s[0] = str(int (ser.readline(),10))
        except:
            s[0] = str(int (ser.readline(),16))
        # print("Again")
        print(s[0])
        seconds2 = 0
        if(int(s[0])>500):   # 490
            start_time_front = time.time()
            while seconds <= 5 and final_turn == True:
                print("Final turn again {}".format(final_turn))
                # print(final_turn)
                # print("Move Forwards")
                # print(seconds)
                motor1.moveF(100)
                motor2.moveF(100)
                # motor1.stop()
                # motor2.stop()
                end_time_front = time.time()
                seconds = end_time_front - start_time_front
                read_serial=ser.readline()
                try:
                    s[0] = str(int (ser.readline(),10))
                except:
                    s[0] = str(int (ser.readline(),16))
                flag = 1
                
            # motor1.moveF(70)
            # motor2.moveF(70)
            '''
            start_time2 = time.time()
            while seconds2 <= 2:
                print(seconds2)
                motor1.stop()
                motor2.stop()
                end_time2 = time.time()
                seconds = end_time2 - start_time2
                read_serial=ser.readline()
                s[0] = str(int (ser.readline(),10))
            '''
            
            # motor1.stop()
            # motor2.stop()
            '''
            start_time2 = time.time()
            while seconds2 <= 5:
                print(seconds2)
                motor1.moveF(60)
                motor2.moveF(60)
                end_time2 = time.time()
                seconds2 = end_time2 - start_time2
                read_serial=ser.readline()
                s[0] = str(int (ser.readline(),10))
            '''
        motor1.stop()
        motor2.stop()
        GPIO.cleanup()
        # motor1.stop()
        # motor2.stop()
except:
        motor1.stop()
        motor2.stop()
        GPIO.cleanup()
        
    
    

'''
while True:
#     GPIO.output(In1,GPIO.LOW)
#     GPIO.output(In2,GPIO.HIGH)
#     pwm.ChangeDutyCycle(50)
    read_serial=ser.readline()
    s[0] = str(int (ser.readline(),10))
    print(s[0])
    if(int(s[0])<490):
        motor1.moveR()
        motor2.moveR()
        time.sleep(3000)
        
    x=input()
    
    if x=='w':
        motor1.moveF(70)
        motor2.moveF(70)
        x='z'
    
    elif x=='a':
        motor1.moveL()
        motor2.moveL()
        x='z'
    
    elif x=='s':
        motor1.moveB(70)
        motor2.moveB(70)
        x='z'
    
    elif x=='d':
        motor1.moveR()
        motor2.moveR()
        x='z'
    
    elif x=='t':
        motor1.stop()
        motor2.stop()
        x='z'
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
'''
'''
while 1:
    read_serial=ser.readline()
    s[0] = str(int (ser.readline(),10))
    print(s[0])
    for event in pygame.event.get(): # User did something
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        if event.type == pygame.JOYAXISMOTION:
            print("Joystick JOYAXISMOTION.")

    print(_joystick.get_axis(0))
    print(_joystick.get_button(0))
    
    buttons = _joystick.get_numbuttons()
    for i in range(buttons):
        button = _joystick.get_button(i)
        print("Button {:>2} value: {}".format(i,button))

    axes = _joystick.get_numaxes()
    print("Number of axes: {}".format(axes))

    for i in range( axes ):
        axis = _joystick.get_axis( i )
        print("Axis {} value: {:>6.3f}".format(i, axis))
    if(_joystick.get_button(4)==0.000)and(_joystick.get_button(5)==0.0)and(_joystick.get_axis(5)==0.000)and (_joystick.get_axis(0)==0.000) or (_joystick.get_axis(2)==-1) or (_joystick.get_axis(5)==-1):
        motor1.stop()
        motor2.stop()
        print("stop")
    elif(_joystick.get_button(4)==1):
        motor1.moveF(100)
        motor2.moveF(100)
        print("Forward")
    elif(_joystick.get_button(5)==1):
        motor1.moveB(100)
        motor2.moveB(100)
        print("Backward")
    elif(_joystick.get_axis(0)>0):
        motor1.moveR()
        motor2.moveR()
        print("Right")
    elif(_joystick.get_axis(0)<0):
        motor1.moveL()
        motor2.moveL()
        print("Left")
    #elif(_joystick.get_button()==1):
        
    clock.tick(20)    
'''

