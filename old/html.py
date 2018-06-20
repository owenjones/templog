from datetime import datetime as d
from dateutil.tz import tzlocal

location = "Owen's Room"

with open("temp.log", "r") as log :
  lines = log.readlines()

temp = round(float(lines[-1].strip().split(" ")[1]), 1)

with open("/home/owen/template.html", "r") as f :
  data = f.read()

data = data.replace("{TEMP}", str(temp))
data = data.replace("{TIME}", "{n:%H}:{n:%M}".format(n=d.now(tzlocal())))
data = data.replace("{LOCATION}", location)

if temp > 24.5 :
  range = "hot"
elif temp > 19.5 :
  range = "warm"
else :
  range = "cold"

data = data.replace("{RANGE}", range)

with open("/home/owen/therm/index.html", "w") as f :
  f.write(data)
