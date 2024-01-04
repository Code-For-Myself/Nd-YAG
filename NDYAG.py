import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

nGe = pd.read_csv("TR01.CSV")
s = nGe["[s]"]
U = nGe["CH1[V]"]

plt.grid()
# plt.legend(loc = "upper right" , fancybox = True , frameon = True , edgecolor = "black")
plt.ylabel("Spannung in mV")
plt.xlabel("Zeit in ms")
plt.plot(1000*s, 1000*U)
#plt.scatter(1000 * s[3036:3700], 1000 * U[3036:3700], label='Messwerte', marker='+')
plt.axvline(x=1000*s[3040], ymin=-11, ymax=11, c='red', ls='--')
plt.axvline(x=1000*s[3700], ymin=-11, ymax=11, c='red', ls='--')

popt, pcov = curve_fit(lambda t,a,b: a*np.exp(-b*t)-9.6,  1000*s[3040:3700],  1000*U[3040:3700])

y = popt[0] * np.e ** (popt[1]*(-1000*s[3040:3700]))-9.6
print(popt[0])
print(popt[1])
print(pcov)

#plt.axvline(x=0.5, ymin=-11, ymax=11)
#plt.plot(1000*s[3040:3700], y, c='red', ls='--',label='Fit')
#plt.legend(loc = "upper right" , fancybox = True , frameon = True , edgecolor = "black")
plt.show()

Ge = pd.read_csv("TR02.CSV")
s = Ge["[s]"]
U = Ge["CH2[V]"]

plt.grid()
# plt.legend(loc = "upper right" , fancybox = True , frameon = True , edgecolor = "black")
plt.ylabel("Spannung in V")
plt.xlabel("Zeit in ms")
#plt.plot(1000 * s, U)
#plt.show()
