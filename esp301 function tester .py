import espModeStirring
import time

controller = espModeStirring.espModeStirring("COM3",921600, 1, True, 0.0, [1,2]) # newport controller device, baud rate, default axis, reset, initial position, axes in use

#controller.debug()
controller.empty_errors()

#getpos + setpos
print("Position is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))
controller.setpos(50,1)
controller.setpos(50,2)
print("Position is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))

time.sleep(1)

#setpos2
controller.setpos2(100,100,1,2)
print("\nPosition is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))

time.sleep(2)

#setpos2wait
controller.setpos2wait(150,150,1,2)
print("\nPosition is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))
controller.setpos2wait(200,200,1,2)
print("Position is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))
controller.setpos2wait(250,250,1,2)
print("Position is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))

time.sleep(3)

#getvel+setvel
print("\nVelocity is x : " + str(controller.getvel(1)) + ", y : " + str(controller.getvel(2)))
controller.setvel(100,1)
controller.setvel(100,2)
print("Position is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))
controller.setpos2wait(0,0,1,2)
print("Position is x : " + str(controller.getpos(1)) + ", y : " + str(controller.getpos(2)))
print("Velocity is x : " + str(controller.getvel(1)) + ", y : " + str(controller.getvel(2)))
controller.setvel(50,1)
controller.setvel(50,2)
print("Velocity is x : " + str(controller.getvel(1)) + ", y : " + str(controller.getvel(2)))
controller.setpos2wait(50,50,1,2)

time.sleep(3)

controller.empty_errors()
#controller.debug()