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
