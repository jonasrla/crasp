import RPi.GPIO as GPIO
from time import time
from scipy import pi
import threading
# from numpy import average
GPIO.setwarnings(False)


right_port = 22
left_port = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(right_port, GPIO.IN)
GPIO.setup(left_port, GPIO.IN)

left_f = []
right_f = []
# system_f = 0

lock = threading.Lock()

def right_tach():
    global right_f
    temp1 = time()
    # counter = 0
    # avg = []
    while True:
        lock.acquire()
        GPIO.wait_for_edge(right_port, GPIO.BOTH)
        temp2 = time()
        right_f.append(pi/(18*(temp2 - temp1)))
        temp1 = temp2
        lock.release()
        # counter += 1
        # avg.append(right_f)
        # if counter == 36:
        #   print average(avg)
        #   avg = []
        #   counter = 0


def left_tach():
    global left_f
    temp1 = time()
    # counter = 0
    # avg = []
    while True:
        lock.acquire()
        GPIO.wait_for_edge(left_port, GPIO.BOTH)
        temp2 = time()
        left_f.append(pi/(18*(temp2 - temp1)))
        temp1 = temp2
        lock.release()
        # counter += 1
        # avg.append(left_f)
        # if counter == 36:
        #   print average(avg)
        #   avg = []
        #   counter = 0

def read_left():
    global left_f
    lock.acquire()
    if len(left_f):
        ave = sum(left_f)/len(left_f)
        print 'left len:', len(left_f)
        left_f = []
    else:
        ave = 0
    lock.release()
    return ave

def read_right():
    global right_f
    lock.acquire()
    if len(right_f):
        ave = sum(right_f)/len(right_f)
        print 'right len:', len(right_f)
        right_f = []
    else:
        ave = 0
    lock.release()
    return ave

# def sys_tach():
#   global left_f
#   global right_f
#   while True:
#       sysem_f = (left_f+right_f)/2