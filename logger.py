from datetime import datetime
import config

class Logger(Thread) :
	DB = None
	sensor = "/sys/bus/w1/devices/" + config.sensor + "/w1-slave"

	run = True
	threshold = config.senseTime
	last = 0

	def __init__(self, DB) :
		Thread.__init__(self)
		self.DB = DB

	def run(self) :
		while self.run :
			dt = datetime.now(tzlocal())
			if dt > self.last + threshold :
				self.last = dt
				self.log()
			sleep(0.01)

	def stop(self) :
		self.run = False

	def log(self) :
		rawtemp = sys("cat {}".format(sensor))
		time = time.now()
