from threading import Thread
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as pyplot
import matplotlib.dates as dates
from matplotlib.ticker import MultipleLocator
from datetime import datetime as d

class Output(Thread) :
	DB = None
	generateHtml = False
	generateGraphs = False

	#             HTML, Day,  Week,  Month, Year
	last =       [0,    0,    0,     0,     0]
	thresholds = [120,  60,   720,   1440,  1440]

	def __init__(self, DB, html, graphs) :
		Thread.__init__(self)
		self.DB = DB
		self.generateHtml = html
		self.generateGraphs = graphs

	def run(self) :
		pass

	def tick(self, time) :
		pass

	def getTemps(self, number) :
		pass

	def html(self, tick) :
		c = self.DB.cursor()
		c.execute("SELECT temperature FROM temperatures ORDER BY time DESC LIMIT 1")
		temp = c.fetchone()

		with open("") as file :
			f = file.read()

		f = f.replace("{TEMP}", str(temp))
		f = f.replace("{TIME}", "{n:%H}:{n:%M}".format(n=d.now(tzlocal())))
		f = f.replace("{LOCATION}", config.location)

		if temp > 24.5 :
		  range = "hot"
		elif temp > 19.5 :
		  range = "warm"
		else :
		  range = "cold"

		f = f.replace("{RANGE}", range)

		self.last[0] = tick

	def today(self, tick) :

		self.last[1] = tick

	def week(self, tick) :

		self.last[2] = tick

	def month(self, tick) :

		self.last[3] = tick

	def year(self, tick) :

		self.last[4] = tick
