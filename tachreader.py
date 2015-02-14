import RPi.GPIO as GPIO
from time import clock

right_port = 22
left_port = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(right_port, GPIO.IN)
GPIO.setup(left_port, GPIO.IN)

left_f = 0
right_f = 0

def right_tach():
	global right_f
	temp1 = 0
	while True:
		GPIO.wait_for_edge(right_port, GPIO.BOTH)
		temp2 = clock()
		right_f = 1/(temp2 - temp1)
		temp1 = temp2


def left_tach():
	global left_f
	temp1 = 0
	while True:
		GPIO.wait_for_edge(left_port, GPIO.BOTH)
		temp2 = clock()
		left_f = 1/(temp2 - temp1)
		temp1 = temp2