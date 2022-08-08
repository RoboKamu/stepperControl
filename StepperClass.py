import time
import RPi.GPIO as gpio

class StepperControls:

    def __init__(self, pins, direction):
        self.pins = pins
        self.direction = direction
        # create global variable for the fullstep sequence
        global seq
        seq = [
            [1, 1, 0, 0], 
            [0, 1, 1, 0], 
            [0, 0, 1, 1], 
            [1, 0, 0, 1] 
            ]
        
      

    def setup(self):
        gpio.setmode(gpio.BOARD)
        # setup output pins and set output to 0
        for pin in self.pins:
            gpio.setup(pin, gpio.OUT)
            gpio.output(pin, 0)
            
    def forward(self):
        print("Moving forward...")
        # Move forward
        while 1:
            for fullstep in range(4):
                for pin in range(4):
                    gpio.output(self.pins[pin], seq[fullstep][pin])
                    time.sleep(0.001)

    def back(self):
        print("Moving backwards...")
        # reverse the direction of previous function
        time.sleep(0.001)
        while 1:
            for fullstep in range(4):
                for pin in range(4):
                    # inverse to pins array to iterate through the array backwards; making it go reverse
                    gpio.output(self.pins[::-1][pin], seq[fullstep][pin])
                    time.sleep(0.001)
    
    def stop(self):
        print("stopped")
        time.sleep(0.001)
        gpio.cleanup()
                
