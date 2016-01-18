import os, time, sys, subprocess, copy, threading, json, requests, socket, random
from flask import Flask, send_from_directory, request

app = Flask(__name__)

messages = []

@app.route("/alive")
def appendAlive():
	global messages
	messages.append(time.time())
	return ""

@app.route("/")
def showMessages():
	global messages
	stat = "{messages: %s, \n number: %s}" % (messages, len(messages))
	return stat

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=int(port), use_reloader=False)
	
