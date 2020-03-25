import matplotlib.pyplot as plt
import numpy as np

data_len = 20

# Growing
healthy = np.zeros(data_len)
dead = np.zeros(data_len)
recovered = np.zeros(data_len)
infected = np.zeros(data_len)
proven = np.zeros(data_len) # Tested and proven infected

# Underlying
infection_rate = 1.325
testing_rate = 53. / 100.

# Initial
region = "Norway"
healthy[0] = 5494000
infected[0] = 10
highest_infection_total = 10

# Growth
for i in range(1, data_len):
    infected[i] = infected[i - 1] * infection_rate
    healthy[i] = healthy[0] - infected[i]
    proven[i] = infected[i] * testing_rate
    if infected[i] > highest_infection_total:
        highest_infection_total = infected[i]

x = np.linspace(0, data_len, data_len)
plt.plot(x, infected)
plt.plot(x, proven)
plt.plot(x, healthy)
plt.ylim(0, highest_infection_total + 100)
plt.xlim(0, data_len)
plt.grid()
plt.title(region)
plt.show()
