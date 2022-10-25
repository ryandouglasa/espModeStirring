import espModeStirring
import time
controller = espModeStirring.espModeStirring("COM3",921600,1) # newport controller device, baud rate, default axis 

#takes an array of any length where each element is a 3-element array in the format [x, y, waitTime]
#and makes the controller visit each point and wait for the time given (seconds)
def multiMotion(array):
    for subArray in array:
        controller.setpos2(subArray[0],subArray[1], 1, 2)
        time.sleep(subArray[2])

#testbench
coordinates = [
    [100, 50, 1],
    [50, 100, 2],
    [25, 75, 3],
    [300, 300, 5],
    [50, 50, 0]
]

controller.debug()
multiMotion(coordinates)
controller.debug()
multiMotion(coordinates)
controller.reset(1)
controller.reset(2)