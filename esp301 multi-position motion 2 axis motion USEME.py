import espModeStirring
import time
controller = espModeStirring.espModeStirring("COM3",921600, 1, True, 50.0, [1,2]) # newport controller device, baud rate, default axis, reset, initial position, axes in use

#takes an array of any length where each element is a 3-element array in the format [x, y, waitTime]  
#and makes the controller visit each coordinate and wait for the time given (seconds)
def multiMotion(array):
    for subArray in array:
        controller.setpos2wait(subArray[0],subArray[1], 1, 2)
        print("now waiting for %d seconds"%(subArray[2]))
        time.sleep(subArray[2])

#testbench
coordinates = [
    [80, 50, 7],
    [110, 50, 7],
    [140, 50, 10],
    [140, 80, 7],
    [140, 110, 7],
    [140, 140, 7]
]

#controller.empty_errors()

controller.setvel(10,1)
controller.setvel(10,2)

#controller.debug()
multiMotion(coordinates)
#controller.debug()

#controller.empty_errors()

#resets position
controller.setpos2(0,300,1,2)
