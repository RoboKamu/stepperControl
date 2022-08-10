import time
import RPi.GPIO as gpio

class StepperControls:

    def __init__(self, pins, direction):
        # self.pins is the 2d list which consist of the pins for each stepper
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
        gpio.cleanup()
        gpio.setmode(gpio.BOARD)
        # setup output pins and set output to 0
        for stepperPins in self.pins:
            for pin in stepperPins:
                gpio.setup(pin, gpio.OUT)
                gpio.output(pin, 0)
            
    def forward(self):
        print("Moving forward...")
        # Move forward
        try:
            while 1:
                for fullstep in range(4):
                    for arr in range(2):
                        for pin in range(4):
                            gpio.output(self.pins[arr][pin], seq[fullstep][pin])
                            time.sleep(0.001)
        except:
            pass    # RuntimeError, stop() cleaned up pins so no pins availabe
        
    def back(self):
        print("Moving backwards...")
        # reverse the direction of previous function
        try:
            # reverse the self.pins 2d array
            reverseArr = [i[::-1] for i in self.pins[::-1]]
            while 1:
                 for fullstep in range(4):
                    for arr in range(2):
                        for pin in range(4):
                            gpio.output(reverseArr[arr][pin], seq[fullstep][pin])
                            time.sleep(0.001)
        except:
            pass    # RuntimeError, stop() cleaned up pins so no pins availabe
    
    def stop(self):
        print("stopped")
        time.sleep(0.001)
        gpio.cleanup()
                
