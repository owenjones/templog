from threading import Thread
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as pyplot
import matplotlib.dates as dates
from matplotlib.ticker import MultipleLocator
from datetime import datetime as d
import config

class Output(Thread) :
	DB = None
	generateHtml = False
	generateGraphs = False

	#             HTML, Day,  Week,  Month, Year
	last =       [0,    0,    0,     0,     0]
	thresholds = [120,  60,   720,   1440,  1440]

	def __init__(self, DB) :
		Thread.__init__(self)
		self.DB = DB

	def run(self) :
		pass

	def tick(self, time) :
		pass

	def getTemps(self, number) :
		number = (number, )
		c = self.DB.cursor()
		c.execute("SELECT temperature FROM temperatures ORDER BY time DESC LIMIT ?", number)
		return c.fetchall()

	def html(self, tick) :
		with open("") as file :
			data = file.read()

		data = data.replace("{TEMP}", str(temp))
		data = data.replace("{TIME}", "{n:%H}:{n:%M}".format(n=d.now(tzlocal())))
		data = data.replace("{LOCATION}", config.location)

		if temp > 24.5 :
		  range = "hot"
		elif temp > 19.5 :
		  range = "warm"
		else :
		  range = "cold"

		data = data.replace("{RANGE}", range)

		with open("/home/owen/therm/index.html", "w") as f :
		  f.write(data)

		self.last[0] = tick

	def today(self, tick) :

		self.last[1] = tick

	def week(self, tick) :

		self.last[2] = tick

	def month(self, tick) :

		self.last[3] = tick

	def year(self, tick) :

		self.last[4] = tick
