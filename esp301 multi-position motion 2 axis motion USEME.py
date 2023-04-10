import espModeStirring
import time
controller = espModeStirring.espModeStirring("COM8",921600, 1, True, 50.0, [1,2]) # newport controller device, baud rate, default axis, reset, initial position, axes in use

#takes an array of any length where each element is a 3-element array in the format [x, y, waitTime]  
#and makes the controller visit each coordinate and wait for the time given (seconds)
def multiMotion(array):
    for subArray in array:
        controller.setpos2(subArray[0],subArray[1], 1, 2)
        waiting = controller.TX()
        while (waiting != (b'@\r\n')):
            time.sleep(0.5)
            waiting = controller.TX()
        print("now waiting for %d seconds"%(subArray[2]))
        time.sleep(subArray[2])

#testbench
coordinates = [
    [50, 0, 2],
    [55, 0, 2],
    [60, 0, 2],
    [65, 0, 2],
    [70, 0, 2],
    [75, 0, 2],
    [80, 0, 2],
    [85, 0, 2]
]

#controller.empty_errors()

#controller.setvel(10,1)
#controller.setvel(10,2)

controller.debug()
multiMotion(coordinates)
controller.debug()

controller.empty_errors()

#resets position
controller.setpos2(50,0,1,2)
