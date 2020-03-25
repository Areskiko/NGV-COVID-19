#region Import
import matplotlib.pyplot as plt
import datetime
from dataAcquisition import getDB
#endregion Import

keysList, data = getDB()
keys = {key:keysList.index(key) for key in keysList}
#Province/State, Country/Region, Last Update, Confirmed, Deaths, Recovered, Latitude, Longitude

TargetType =        "Country/Region"
TargetLocation =    "Norway"
Target =            "Confirmed"


#region Data
plotPointsx = [datetime.datetime.strptime(row[0],r"%d-%m-%Y").date() for row in data]

plotPointsy = []
for row in data:
    found = False
    for place in row[1][:-1]:
        if place[keys[TargetType]] == TargetLocation:
            plotPointsy.append(int(place[keys[Target]]))
            found = True
    if not found:
        plotPointsy.append(0)
#endregion Data

plt.plot(plotPointsx, plotPointsy)
plt.show()
