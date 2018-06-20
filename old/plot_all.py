import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as p
import matplotlib.dates as da
from matplotlib.ticker import MultipleLocator
from datetime import datetime as d

with open("temp.log", "r") as log :
  lines = log.readlines()

lines = [x.strip().split(" ") for x in lines]

times = []
temps = []

for line in lines :
  times.append(d.fromtimestamp(int(line[0].strip("[]"))))
  temps.append(float(line[1]))

#times = times[-288:]
#temps = temps[-288:]
upper = max(temps) + 1
lower = min(temps) - 1

p.plot(times, temps, "r")
axes = p.gca()
axes.set_ylim([lower, upper])
p.title("All Measurements")
#p.xticks(rotation="vertical")

f = da.DateFormatter("%j")
axes.xaxis.set_major_formatter(f)
axes.yaxis.set_minor_locator(MultipleLocator(1))
axes.grid(which="both", linestyle="--", linewidth=0.5)
#p.gcf().autofmt_xdate()

p.savefig("/home/owen/therm/graph_all.png")
