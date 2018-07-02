class Logger(Thread) :
	sensor = ""

	last = 0
	threshold = 60

	def __init__(self, sensor) :
		Thread.__init__(self)
		self.sensor = "/sys/bus/w1/devices/" + sensor + "/w1-slave"

	def run(self) :
