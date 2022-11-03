import espModeStirring
import time
controller = espModeStirring.espModeStirring("COM3",921600, 1, True, 0.0, [1,2]) # newport controller device, baud rate, default axis, reset, initial position, axes in use

#takes an array of any length where each element is a 3-element array in the format [x, y, waitTime]
#and makes the controller visit each coordinate and wait for the time given (seconds)
def multiMotion(array):
    for subArray in array:
        controller.setpos2(subArray[0],subArray[1], 1, 2)
        print("now waiting for %d seconds"%(subArray[2]))
        time.sleep(subArray[2])

#testbench
coordinates = [
    [100, 50, 1],
    [50, 100, 2],
    [25, 75, 3],
    [300, 300, 5],
    [50, 50, 0]
]

big_dist_big_wait = [[300,300,5]]

controller.empty_errors()

controller.debug()
#multiMotion(big_dist_big_wait)
multiMotion(coordinates)
controller.debug()

controller.setpos2(0,0,1,2)

controller.reset(1)
controller.reset(2)
