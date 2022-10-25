import serial

class espModeStirring:
	def __init__(self, dev="COM3", b=921600,axis=1,reset=True, initpos = 0.0,useaxis=[]):
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
					print("Error while setting up controller, error # %d"%r)
				if(initpos!=0):
					self.setpos(initpos)
					r = self.check_errors()
					if(r!=0):
						print("Error while setting up controller, error # %d"%r)


	#RD: changes debug variable to the opposite of its current state, default state is 0
	def debug(self):
		if self.bugVar == 1:
			self.bugVar = 0
		else:
			self.bugVar = 1

	def reset(self,axis):
		self.dev.write(b"%dOR;%dWS0\r"%(axis,axis))
	
	def check_errors(self):
		self.dev.write(b"TE?\r")
		return float(self.dev.readline())

	def getpos(self,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		self.dev.write(b"%dTP\r"%a)
		return float(self.dev.readline())
	
	def setpos(self,pos,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		if self.bugVar == 1:
			print("setting postition to %f"%pos)
		self.dev.write(b"%dPA%.4f;%dWS1;%dTP\r"%(a,pos,a,a))
		return float(self.dev.readline())

	#RD: accepts x,y coordinates and sends to controller
	def setpos2(self, posx, posy, axis1=None, axis2=None):
		a = axis1
		b = axis2
		if self.bugVar == 1:
			print("setting postition to x : %f, y : %f"%(posx, posy))
		self.dev.write(b"%dPA%.4f;%dPA%.4f;%dWS1;%dWS1;%dTP;%dTP\r"%(a,posx,b,posy, a, b, a, b))
		return float(self.dev.readline())

	#RD: accepts axis and returns velocity setting of the axis
	def getvel(self,axis=None):
		a=self.defaxis
		if(axis and axis>0):
			a = axis
		self.dev.write(b"%dVA?\r"%a)
		return float(self.dev.readline())

	#RD: accepts axis and new velocity setting for axis, sets axis velocity to input
	def setvel(self,vel,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		if self.bugVar == 1:
			print("setting velocity to %f"%vel)
		self.dev.write(b"%dVA%f;%dVA?\r"%(a,vel,a))
		return float(self.dev.readline())

	def position(self,pos=None,axis=None):
		if(isinstance(pos,(float,int))):
			self.setpos(pos,axis)
			self.getpos()
			self.setpos(pos,axis)
		return self.getpos(axis)