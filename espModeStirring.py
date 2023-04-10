import serial

class espModeStirring:
	def __init__(self, dev="COM8", b=921600,axis=1,reset=True, initpos = 0.0,useaxis=[]):
		self.dev = serial.Serial(dev,b)
		self.inuse = useaxis
		self.bugVar = 0
		if(len(self.inuse)==0):
			self.inuse = [axis]
		self.defaxis = axis
		if(reset):
			for n in self.inuse:
				self.reset(n)
				r = self.check_errors()
				if(r!=0):
					print("ESP controller error # %d"%r)
				if(initpos!=0):
					self.setpos(initpos)
					r = self.check_errors()
					if(r!=0):
						print("ESP controller error # %d"%r)


	#RD: changes debug variable to the opposite of its current state, default state is 0
	def debug(self):
		if self.bugVar == 1:
			self.bugVar = 0
		else:
			self.bugVar = 1

	#RD: reads all errors, emptying error queue in controller
	def empty_errors(self):
		for i in range(10):
			errNum = self.check_errors()
			if(errNum != 0):
				print("ESP controller error # %d"%errNum)
			else:
				print("No errors in ESP controller")

	#RD: send TB command to controller
	def tell_buffer(self):
		self.dev.write(b"TB?\r")
		line = self.dev.readline()
		print(line)

	def reset(self,axis):
		self.dev.write(b"%dWS0;%dOR;%dWS0\r"%(axis,axis,axis))
	
	def check_errors(self):
		self.dev.write(b"TE?\r")
		return float(self.dev.readline())

	def getpos(self,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		command = b"%dTP\r"%a
		if self.bugVar == 1:
			print("command sent to controller is ->" + str(command, 'ASCII'))
		self.dev.write(command)
		line = self.dev.readline()
		if self.bugVar == 1:
			print("returned ->" + str(line))
		return float(line)
	
	def setpos(self,pos,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		command = b"%dWS0;%dPA%.4f;%dWS0;%dTP\r"%(a,a,pos,a,a)
		if self.bugVar == 1:
			print("setting axis %d postition to %f"%(a,pos))
			print("command sent to controller is ->" + str(command, 'ASCII'))
		self.dev.write(command)
		line = self.dev.readline()
		if self.bugVar == 1:
			print("stage should be in position now")
			print("returned ->" + str(line))
		return float(line)

	#RD: accepts x,y coordinates in millimeters and sends to controller
	def setpos2(self, posx, posy, axis1=None, axis2=None):
		a = axis1
		b = axis2
		command = b"%dWS0;%dWS0;%dPA%.4f;%dPA%.4f;%dWS0;%dWS0;%dTP;%dTP\r"%(a,b,a,posx,b,posy, a, b, a, b)
		if self.bugVar == 1:
			print("setting postition to x : %f, y : %f "%(posx, posy))
			print("command sent to controller is ->" + str(command, 'ASCII'))
		self.dev.write(command)
		line = self.dev.readline()
		line2 = self.dev.readline()
		if self.bugVar == 1:
			print("stage should be in position now")
			print("returned ->" + str(line))
			print("returned ->" + str(line2))
		return float(line)
	
	#RD: accepts x,y coordinates in millimeters, sends commands to controller
	#only works as desired with semicolon in front, but that puts an error in the buffer
	def setpos2wait(self, posx, posy, axis1=None, axis2=None):
		a = axis1
		b = axis2
		command = b";%dWS0;%dWS0;%dPA%.4f;%dPA%.4f;%dWS0;%dWS0;%dTP;%dTP\r"%(a, b, a, posx, b, posy, a, b, a, b)
		if self.bugVar == 1:
			print(" setting postition to x : %f, y : %f"%(posx, posy))
			print("command sent to controller is ->" + str(command, 'ASCII'))
		self.dev.write(command)
		line = self.dev.readline()
		if self.bugVar == 1:
			print("stage should be in position now")
			print("returned ->" + str(line))
		#the 2 lines of code below delete the ESP error #6 thrown every time setpos2wait is called,
		#this error is thrown because of the semicolon at the beginning of command, but the desired behavior
		#doesn't happen without that semicolon
		self.dev.write(b"TE?\r")
		self.dev.readline()
		return float(line)
	
	#RD:Sends TX to contoller
	# 	Example usage from user program

	#	(movement command)
	#	variable = controller.TX()
	#	while (variable != (b'@\r\n')):    // @ = 01000000
	#		time.sleep(0.5)
	#		variable = controller.TX()
	def TX(self,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		command = b"TX\r"
		if self.bugVar == 1:
			print("Sending Command bits: " + str(command) + "to controller")
			print("command sent to controller is ->" + str(command, 'ASCII'))
		self.dev.write(command)
		line = self.dev.readline()
		if self.bugVar == 1:
			print("returned ->" + str(line))
		return line

	#RD: accepts axis and returns velocity setting of the axis
	def getvel(self,axis=None):
		a=self.defaxis
		if(axis and axis>0):
			a = axis
		command = b"%dVA?\r"%a
		if self.bugVar == 1:
			print("command sent to controller is ->" + str(command, 'ASCII'))
		self.dev.write(command)
		line = self.dev.readline()
		if self.bugVar == 1:
			print("returned ->" + str(line))
		return float(line)

	#RD: accepts axis and new velocity setting for axis, sets axis velocity to input
	def setvel(self,vel,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		command = b"%dWS0;%dVA%f;%dVA?\r"%(a,a,vel,a)
		if self.bugVar == 1:
			print("setting axis %d velocity to %f"%(a, vel))
			print("command sent to controller is ->" + str(command, 'ASCII'))
		self.dev.write(command)
		line = self.dev.readline()
		if self.bugVar == 1:
			print("returned ->" + str(line))
		return float(line)


	def position(self,pos=None,axis=None):
		if(isinstance(pos,(float,int))):
			self.setpos(pos,axis)
			self.getpos()
			self.setpos(pos,axis)
		return self.getpos(axis)
