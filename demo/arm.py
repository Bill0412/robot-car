import serial
from FractalMind import *
import cv2
import time
import RPi.GPIO as GPIO

def servo_power_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)

ser = serial.Serial("/dev/serial0", 9600)

hold_angle = {
    'beer': 45,
    'yangleduo': 35,
    'shuangwaiwai': 40,
    'deluxe': 50,
    'red_bull': 50,
    'block': 52
    }



def hold(item_name,func=None, t=10):
    if item_name in hold_angle.keys():    
        servo(6, hold_angle[item_name], 40)
        if func != None:
            func()
        time.sleep(t)
        return
    
    print('ERR(in hold_item): item not found')
    
def release(t=3):
    servo(6, 75, 40)
    time.sleep(t)
    
def test_all():

    servo(3, 23, 40)
    time.sleep(0.5)
    servo(3, 70, 40)
    time.sleep(0.5)
    servo(2, 140, 40)
    time.sleep(0.4)
    servo(2, 160, 40)
    servo(1, 0, 40)
    time.sleep(0.5)
    servo(1, 90, 40)
    time.sleep(0.6)
    servo(4, 60, 40)
    time.sleep(0.3)
    servo(4, 96, 40)
    time.sleep(0.3)
    servo(6, 40, 40)
    time.sleep(2)
    servo(6, 70, 40)
    time.sleep(0.5)
    servo(5, 0, 40)
    time.sleep(0.3)
    servo(5, 180, 40)
    time.sleep(0.3)

def init(first_servo_angle=90):
    servo(1, 90)
    servo(2, 180)
    servo(3, 90)
    servo(4, 90)
    servo(5, 30, 40)
    servo(6, 30, 40)
    
def catch_things(direction_index,which_thing):
    things=['block','cube','redBull','tennis','leHu','coolYY','milk','ADmilk','beer','yakult']
    force=[60,70,90,50,40,30,20,50,90,63]
    #need to test the value of angle
    direction=[80,120,80,40]
    #need to test the value of angle
    servo(1, direction[direction_index], 40)
    servo(2, 180, 40)
    servo(3, 110, 40)
    servo(4, 140, 40)
    servo(5, 30, 40)
    servo(6, 30, 40)
    time.sleep(0.3)
    servo(6, force[things.index(which_thing)], 40)
    time.sleep(9999)
    
def put_things():
    servo(1, 80, 40)
    servo(2, 180, 40)
    servo(3, 110, 40)
    servo(4, 120, 40)
    servo(5, 30, 40)
    servo(6, 30, 40)
    
def adjust_for_side_shelf():
    servo(1, 0)
    servo(2, 90, t=0)
    servo(3, 140, t=0)
    servo(4, 130)
    #servo(3, 80)
    
def back_init(first_servo_angle=90):
    servo(4, 30, t=1)
    servo(1, first_servo_angle)
    servo(2, 75, t=0)
    servo(3, 110, t=0)
    init()
    

def servo(n, angle, speed=40, t=0.2):
    if n == 2 and angle > 140:
        angle = 140
    if n in (2, 3, 4):
        d = {
            2: 225,
            3: 200,
            4: 250
        }
        angle = d[n] - angle
    if n == 1 and angle < 5:
        angle = 5
    ser.write(GetMessage(n, angle, speed))
    time.sleep(t)
    
#while True:
#init()
    
# time.sleep(1)
   # adjust_for_side_shelf()
# ser.write(GetMessage(2, 85,  40))
#servo(2, 1)
#time.sleep(0.5)
#hold('beer', func=adjust_for_side_shelf)
#release()
#back_init()
# servo(4, 60)
#servo(3, 90)
# servo(4, 50)
    #if cv2.waitKey(5) & 0xff == ord('q'):
      #  break




servo_power_on()
init()
GPIO.cleanup()
    
    
    
    
    
    
    