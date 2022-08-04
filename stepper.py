import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

# setup pins
usedPins = [7, 11, 13, 15]
for pin in usedPins:
  gpio.setup(pin, gpio.OUT)
  gpio.output(pin, 0);
  
try:
  seq = [ 
         [1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [1, 0, 0, 1] 
       ]

  # fullstep, 4 cycles, 1/64 gear reduction
  # 4*64 = 256, one resolution
  print("clockwise")
  for i in range(256):
    for fullstep in range(4):
      for pin in range(4):
       gpio.output(usedPins[pin], seq[fullstep][pin])
       time.sleep(0.001)
        
  time.sleep(0.5)
  
  print("counterclockwise")
  for i in range(256):
    for fullstep in range(3, 0, -1):
      for pin range(3, 0, -1):
        gpio.output(usedPins[pin], seq[fullstep][pin])
        time.sleep(0.001)
  
finally:
  gpio.cleanup()
  print("done");
