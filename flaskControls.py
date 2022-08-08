import RPi.GPIO as gpio
import time

from flask import Flask, redirect, url_for, render_template, request
from StepperClass import StepperControls

app = Flask(__name__)
gpio.setwarnings(False)

try:
    @app.route("/", methods=["POST", "GET"])
    def home():
        test = StepperControls([7, 11, 13, 15], "S")
        test.stop()
        return render_template("index.html")

    @app.route("/F")
    def forward():
        try:
            test = StepperControls([7, 11, 13, 15], "F")
            test.setup()
            test.forward()
            return render_template("forward.html")
        finally:
            gpio.cleanup()

    @app.route("/B")
    def back():
        test = StepperControls([7, 11, 13, 15], "B")
        test.setup()
        test.back()
        return render_template("backward.html")

    @app.route("/L")
    def left():
        return render_template("left.html")

    @app.route("/R")
    def right():
        return render_template("right.html")
except:
    print("Runtime Error")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port="5000")
