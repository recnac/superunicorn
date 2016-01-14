import os, time, sys, subprocess, copy, threading, json, requests, socket, random
from flask import Flask, send_from_directory, request

app = Flask(__name__)

primes = []
noprimes = []

@app.route("/primes")
def returnPrimes():
	global primes
	return (",").join(primes)

@app.route("/noprimes")
def returnNoPrimes():
	global noprimes
	return (",").join(noprimes)
	
@app.route("/getjob")
def giveJob():
	return str(random.randint(1, 5000))
	
@app.route("/prime")
def getPrime():
	global primes
	primes.append(request.url.split("?number=")[1])
	return ""

@app.route("/noprime")
def getNoPrime():
	global noprimes
	noprimes.append(request.url.split("?number=")[1])
	return ""

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=int(port), use_reloader=False)
	
