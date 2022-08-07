import RPi.GPIO as gpio
import time

from flask import Flask, redirect, url_for, render_template
from StepperClass import StepperControls

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    test = StepperControls([7, 11, 13, 15], "S")
    test.stop()
    return render_template("index.html")

@app.route("/F")
def forward():
    test = StepperControls([7, 11, 13, 15], "F")
    test.forward()
    return render_template("forward.html")

@app.route("/B")
def back():
    test = StepperControls([7, 11, 13, 15], "B")
    test.back()
    return render_template("backward.html")

@app.route("/L")
def left():
    return render_template("left.html")

@app.route("/R")
def right():
    return render_template("right.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

'''
# {{url}}/led?status=on
@app.route('/', methods=['GET'])
def led():
    status = request.args.get('status')
    if status == "on":
        GPIO.output(18, GPIO.HIGH)
        return jsonify({"message": "Led successfully turned on"})
    elif status == "off":
        GPIO.output(18, GPIO.LOW)
        return jsonify({"message": "Led successfully turned off"})
    else:
        return jsonify({"message": "Not a valid status"})
'''
