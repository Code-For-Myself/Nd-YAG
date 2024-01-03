import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nGe = pd.read_csv("TR01.CSV")
s = nGe["[s]"]
U = nGe["CH1[V]"]


plt.grid()
#plt.legend(loc = "upper right" , fancybox = True , frameon = True , edgecolor = "black")
plt.ylabel("Spannung in mV")
plt.xlabel("Zeit in ms")
plt.plot(1000*s,1000*U)
plt.show()