import RPi.GPIO as GPIO
from time import time
# from scipy import pi
import threading
# from numpy import average
GPIO.setwarnings(False)


right_port = 22
left_port = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(right_port, GPIO.IN)
GPIO.setup(left_port, GPIO.IN)

counter_left = 0
counter_right = 0
begin_time_left = 0
begin_time_right = 0
end_time_left = 0
end_time_right = 0
# system_f = 0

lock = threading.Lock()

def right_tach():
    global counter_right
    global begin_time_right
    global end_time_right
    begin_time_right = time()
    # counter = 0
    # avg = []
    while True:
        lock.acquire()
        GPIO.wait_for_edge(right_port, GPIO.BOTH)
        end_time_right = time()
        counter_right += 1
        lock.release()
        # counter += 1
        # avg.append(right_f)
        # if counter == 36:
        #   print average(avg)
        #   avg = []
        #   counter = 0


def left_tach():
    global counter_left
    global begin_time_left
    global end_time_left
    begin_time_left = time()
    # counter = 0
    # avg = []
    while True:
        lock.acquire()
        GPIO.wait_for_edge(left_port, GPIO.BOTH)
        end_time_left = time()
        counter_left += 1
        lock.release()
        # counter += 1
        # avg.append(left_f)
        # if counter == 36:
        #   print average(avg)
        #   avg = []
        #   counter = 0

def read_left():
    global counter_left
    global begin_time_left
    global end_time_left
    if counter_left:
        lock.acquire()
        ave = (3.14*counter_left)/(9*(end_time_left-begin_time_left))
        begin_time_left = end_time_left
        counter_left = 0
        lock.release()
    else:
        ave = 0
    return ave

def read_right():
    global counter_right
    global begin_time_right
    global end_time_right
    if counter_right:
        lock.acquire()
        ave = (3.14*counter_right)/(9*(end_time_right-begin_time_right))
        begin_time_right = end_time_right
        counter_right = 0
        lock.release()
    else:
        ave = 0
    return ave

# def sys_tach():
#   global left_f
#   global right_f
#   while True:
#       sysem_f = (left_f+right_f)/2