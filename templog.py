# Overall app layout -
# * Launcher (this file), takes a few flags, inits SQLite DB, launches relevant threads - watchdog for those
# * Temperature Logging Thread - takes a reading every minute and stores it
# * Output Thread - creates graphs and html output

import sqlite3
import config
from logger import Logger
from output import Output

DB = None

def connectDB() :
    DB = sqlite3.connect(config.db)

def newDB() :
    pass

def startLogger() :
	pass

def startOutput() :
	pass

if __name__ == "__main__" :
	# TODO: Input arguments to generate a new DB, and possibly enter some of the config details?

	connectDB()
	l = Logger(DB)
	o = Output(DB)
	l.start()
	o.start()

	run = True
	while run :
		t = Threading.enumerate()
		# Not sure what's going on around here - I guess just checking both threads are still running and restarting them if they're not?
		sleep(10)
