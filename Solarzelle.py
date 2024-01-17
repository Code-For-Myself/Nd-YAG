import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


data = pd.read_csv("Grün_525nm_Durchlassrichtung.txt", sep=",")
data2 = pd.read_csv("Grün_525nm_Sperrrichtung.txt", sep=",")
xdata = data[" U in V (mess)"]
ydata = data[" I in mA (mess)"]
xdata2 = data2[" U in V (mess)"]
ydata2 = data2[" I in mA (mess)"]
xdatac = np.concatenate((xdata, xdata2))
ydatac = np.concatenate((ydata, ydata2))
xdatazip = list(zip(xdata, xdata2))
ydatazip = list(zip(abs(ydata), abs(ydata2)))
def Plotter(Pfad, Pfad2, Label, Marker):
    data = pd.read_csv(Pfad, sep=",")
    data2 = pd.read_csv(Pfad2, sep=",")
    xdata = data[" U in V (mess)"]
    ydata = data[" I in mA (mess)"]
    xdata2 = data2[" U in V (mess)"]
    ydata2 = data2[" I in mA (mess)"]
    xdatazip = list(zip(xdata, xdata2))
    ydatazip = list(zip(ydata, ydata2))
    plt.xlabel("Spannung in V")
    plt.ylabel("Strom in mA")
    plt.scatter(xdatazip, ydatazip, label=Label, marker=Marker)
    return 0
def lnPlotter(Pfad, Pfad2, Label, Marker):
    data = pd.read_csv(Pfad, sep=",")
    data2 = pd.read_csv(Pfad2, sep=",")
    xdata = data[" U in V (mess)"]
    ydata = data[" I in mA (mess)"]
    xdata2 = data2[" U in V (mess)"]
    ydata2 = data2[" I in mA (mess)"]
    xdatazip = list(zip(xdata, xdata2))
    ydatazip = list(zip(abs(ydata), abs(ydata2)))
    plt.xlabel("Spannung in V")
    plt.ylabel("Strom in A")
    plt.scatter(xdatazip, np.log10(ydatazip), label=Label, marker=Marker)
    return 0
def Sperrplotter(Pfad, Label, Marker):
    data = pd.read_csv(Pfad, sep=",")
    xdata = data[" U in V (mess)"]
    ydata = data[" I in mA (mess)"]
    plt.xlabel("Spannung in V")
    plt.ylabel("Strom in mA")
    plt.scatter(xdata, ydata, label=Label, marker=Marker)
    return 0

Plotter("Grün_525nm_Durchlassrichtung.txt", "Grün_525nm_Sperrrichtung.txt", "Grün", "+")
Plotter("Rot_630nm_Durchlassrichtung.txt", "Rot_630nm_Sperrrichtung.txt", "Rot", "v")
Plotter("WeißesLicht_60W_Durchlassrichtung.txt", "WeißesLicht_60W_Sperrrichtung.txt", "Weiß", "D")
Plotter("Tageslicht_Durchlassrichtung.txt", "Tageslicht_Sperrrichtung.txt", "Tageslicht", "x")
plt.legend(loc = "upper left" , fancybox = True , frameon = True , edgecolor = "black")
plt.grid()
plt.show()

Sperrplotter("Grün_525nm_Sperrrichtung.txt", "Grün", "+")
Sperrplotter("Rot_630nm_Sperrrichtung.txt", "Rot", "v")
Sperrplotter("WeißesLicht_60W_Sperrrichtung.txt", "Weiß", "D")
Sperrplotter("Tageslicht_Sperrrichtung.txt",  "Tageslicht", "x")
plt.legend(loc = "center left" , fancybox = True , frameon = True , edgecolor = "black")
plt.grid()
plt.show()
# plt.legend(loc = "upper right" , fancybox = True , frameon = True , edgecolor = "black")
lnPlotter("Grün_525nm_Durchlassrichtung.txt", "Grün_525nm_Sperrrichtung.txt", "Grün", "+")

plt.legend(loc = "upper left" , fancybox = True , frameon = True , edgecolor = "black")
plt.grid()
plt.show()
#plt.scatter(xgreenzip, ygreenzip)
#plt.scatter(xrotzip, yrotzip)
#plt.show()


print(popt)
plt.show()