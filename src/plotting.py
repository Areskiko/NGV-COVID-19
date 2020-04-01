#region Import
import matplotlib.pyplot as plt
from dataAcquisition import getDB, extractPoints
#endregion Import

keysList, data = getDB()
keys = {key:keysList.index(key) for key in keysList}
#Province/State, Country/Region, Last Update, Confirmed, Deaths, Recovered, Latitude, Longitude

TargetType =        "Country/Region"
TargetLocation =    "Norway"
Target =            "Confirmed"

x, y, = extractPoints(TargetType, TargetLocation, Target, keys, data)
plt.plot(x, y)
plt.show()
