import serial
from FractalMind import *
import cv2
import time

ser = serial.Serial("/dev/serial0", 9600)

def servo(n, angle, speed):
    if n == 4:
        angle = 180 - angle
    ser.write(GetMessage(n, angle, speed))

def grab_staff():
    servo(6, 45, 40)
    time.sleep(0.5)
    
def release_staff():
    servo(6, 75, 40)
    time.sleep(0.5)
    
    
    
def test_all():
    servo(3, 60, 40)
    time.sleep(0.5)
    servo(3, 40, 40)
    time.sleep(0.5)
    servo(2, 170, 40)
    time.sleep(0.4)
    servo(2, 150, 40)
    servo(1, 0, 40)
    time.sleep(0.5)
    servo(1, 90, 40)
    time.sleep(0.6)
    servo(4, 60, 40)
    time.sleep(0.3)
    servo(6, 40, 40)
    time.sleep(2)
    servo(6, 70, 40)
    time.sleep(0.5)
    


    
while True:
    grab_staff()
    time.sleep(4)
    release_staff()
    
    

