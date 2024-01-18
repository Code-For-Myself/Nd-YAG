import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Funktion Auswertung ist für Rot, Grün, Tageslicht, die andern lassen sich nicht fitten

def Auswertung(Pfad, Pfad2):
    a = 25
    b = 7
    data = pd.read_csv(Pfad, sep=",")
    data2 = pd.read_csv(Pfad2, sep=",")
    xdata = np.array(data[" U in V (mess)"])
    ydata = np.array(data[" I in mA (mess)"])
    xdata2 = np.array(data2[" U in V (mess)"])
    ydata2 = np.array(data2[" I in mA (mess)"])
    xdata2r = xdata2[::-1]
    ydata2r = ydata2[::-1]
    xdatazip = np.concatenate((xdata2r, xdata))
    ydatazip = np.concatenate((ydata2r, ydata))
    for i in range(len(ydatazip)):
        if ydatazip[i] < 0:
            x = i
    print(x)
    xlist = np.linspace(min(xdatazip[a:x + b]), max(xdatazip[a:x + b]), 1000)
    popt, pcov = curve_fit(lambda x, a, b, c: a * (np.exp(x / b) - 1) - c, xdatazip[a:x + b], ydatazip[a:x + b])
    y = popt[0] * (np.e ** (xlist / popt[1]) - 1) - popt[2]
    plt.plot(xlist, y, color="red")
    plt.scatter(xdatazip[a:x + b], ydatazip[a:x + b])
    print(popt)
    ifoto = abs(ydatazip[30])
    for i in range(len(y)):
        if y[i] < 0:
            d = i
    for i in range(len(y)):
        if xlist[i] < 0:
            e = i
    uleer = abs(xlist[d])
    arr = xlist[e+1:d]*y[e+1:d]
    pmax = abs(min(arr))
    sf = 1.12
    ff = pmax/(ifoto*uleer)
    cf = sf * ff
    print("I_Foto: ", ifoto)
    print("U_L: ", uleer)
    print("max Leistung: ", pmax)
    print("Spannungsfaktor: ", sf)
    print("Füllfaktor: ", ff)
    print("cFaktor: ", cf)
    plt.show()
Auswertung("Tageslicht_Durchlassrichtung.txt","Tageslicht_Sperrrichtung.txt")


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

#Plotter("Grün_525nm_Durchlassrichtung.txt", "Grün_525nm_Sperrrichtung.txt", "Grün", "+")
#Plotter("Rot_630nm_Durchlassrichtung.txt", "Rot_630nm_Sperrrichtung.txt", "Rot", "v")
#Plotter("WeißesLicht_60W_Durchlassrichtung.txt", "WeißesLicht_60W_Sperrrichtung.txt", "Weiß", "D")
#Plotter("Tageslicht_Durchlassrichtung.txt", "Tageslicht_Sperrrichtung.txt", "Tageslicht", "x")
#plt.legend(loc = "upper left" , fancybox = True , frameon = True , edgecolor = "black")
plt.grid()
#plt.show()

#Sperrplotter("Grün_525nm_Sperrrichtung.txt", "Grün", "+")
#Sperrplotter("Rot_630nm_Sperrrichtung.txt", "Rot", "v")
#Sperrplotter("WeißesLicht_60W_Sperrrichtung.txt", "Weiß", "D")
#Sperrplotter("Tageslicht_Sperrrichtung.txt",  "Tageslicht", "x")
#plt.legend(loc = "center left" , fancybox = True , frameon = True , edgecolor = "black")
plt.grid()
#plt.show()
# plt.legend(loc = "upper right" , fancybox = True , frameon = True , edgecolor = "black")
#lnPlotter("Grün_525nm_Durchlassrichtung.txt", "Grün_525nm_Sperrrichtung.txt", "Grün", "+")

#plt.legend(loc = "upper left" , fancybox = True , frameon = True , edgecolor = "black")
#plt.grid()
#plt.show()
#plt.scatter(xgreenzip, ygreenzip)
#plt.scatter(xrotzip, yrotzip)
#plt.show()



#plt.show()

