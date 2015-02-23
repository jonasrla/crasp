import socket
from flask import Flask
app = Flask(__name__)


s = socket.socket()
s.connect(('192.168.2.1',23))


msg = ''

def get_message():
	global msg
	msg = s.recv(2048)
	


@app.route('/')
def hello():
	global msg
	get_message()
	return msg

app.run()