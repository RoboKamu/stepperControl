import RPi.GPIO as gpio
import time

from flask import Flask, redirect, url_for, render_template, request
from StepperClass import StepperControls

app = Flask(__name__)
gpio.setwarnings(False)

@app.route("/", methods=["POST", "GET"])
def home():
    move = StepperControls([[7, 11, 13, 15], [31, 33, 35, 37]], "S")
    move.stop()
    return render_template("index.html")

@app.route("/F")
def forward():
    gpio.cleanup()
    move = StepperControls([[7, 11, 13, 15], [31, 33, 35, 37]], "F")
    move.setup()
    move.forward()
    render_template("forward.html")

@app.route("/B")
def back():
    gpio.cleanup()
    move = StepperControls([[7, 11, 13, 15], [31, 33, 35, 37]], "B")
    move.setup()
    move.back()
    return render_template("backward.html")

@app.route("/L")
def left():
    gpio.cleanup()
    move = StepperControls([[7, 11, 13, 15], [31, 33, 35, 37]], "L")
    move.setup()
    move.left()
    return render_template("left.html")

@app.route("/R")
def right():
    gpio.cleanup()
    move = StepperControls([[7, 11, 13, 15], [31, 33, 35, 37]], "R")
    move.setup()
    move.right()
    return render_template("right.html")

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port="5000")
