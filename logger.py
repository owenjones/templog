import config
from threading import Thread

# Overall app layout -
# * Launcher (this script), takes a few flags, inits SQLite DB if needed, launches relevant threads - watchdog for those
# * Temperature Logging Thread - inits DB connection, takes a reading every minute and stores it
# * Output Thread - inits DB connection, creates graphs and html output



class Logger(Thread) :
	def __init__(self) :
		Thread.__init__(self)

	def run(self) :


class Output(Thread) :
	def __init__(self) :
		Thread.__init__(self)

	def run(self) :
		

def newDB() :
    pass

def connectDB() :
    pass

if __name__ == "__main__" :
