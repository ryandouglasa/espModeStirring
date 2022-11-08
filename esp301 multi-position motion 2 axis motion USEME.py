import espModeStirring
import time
controller = espModeStirring.espModeStirring("COM3",921600, 1, False, 300.0, [1,2]) # newport controller device, baud rate, default axis, reset, initial position, axes in use

#takes an array of any length where each element is a 3-element array in the format [x, y, waitTime]
#and makes the controller visit each coordinate and wait for the time given (seconds)
def multiMotion(array):
    for subArray in array:
        controller.setpos2wait(subArray[0],subArray[1], 1, 2)
        print("now waiting for %d seconds"%(subArray[2]))
        time.sleep(subArray[2])

#testbench
coordinates = [
    [0, 0, 1],
    [550, 550, 2],
]

controller.empty_errors()

controller.debug()
multiMotion(coordinates)
controller.debug()

controller.empty_errors()

#resets position
controller.setpos2(300,300,1,2)