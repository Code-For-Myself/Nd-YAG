import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Plotter(Pfad, Pfad2, Label, Marker, Color):
    data = pd.read_csv(Pfad, sep=",")
    data2 = pd.read_csv(Pfad2, sep=",")
    xdata = data[" U in V (mess)"]
    ydata = data[" I in mA (mess)"]
    xdata2 = data2[" U in V (mess)"]
    ydata2 = data2[" I in mA (mess)"]
    xdata2r = xdata2[::-1]
    ydata2r = ydata2[::-1]
    xdatazip = np.concatenate((xdata2r, xdata))
    ydatazip = np.concatenate((ydata2r, ydata))
    plt.xlabel("Spannung in V")
    plt.ylabel("Strom in A")
    plt.plot(xdatazip, ydatazip, label=Label, marker=Marker, ms=0, color=Color)
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
def Sperrplotter(Pfad):
    data = pd.read_csv(Pfad, sep=",")
    xdata = data[" U (V)"]
    ydata = data[" I (A)"]

    #plt.xlabel("Spannung in V")
    #plt.ylabel("Strom in mA")
    #plt.scatter(xdata, ydata, label=Label, marker=Marker, color=Color)
    return xdata, ydata
#Funktion Auswertung ist für Rot, Grün, Tageslicht, die andern lassen sich nicht fitten
Name = []
Fotostrom = []
Uleer = []
maxLeistung = []
Spannungsfaktor = []
Füllfaktor = []
charaktFaktor = []
def Auswertung(Pfad, Pfad2):
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
        if xdatazip[i] < 0:
            x = i
    ifoto = abs((ydatazip[x]+ydatazip[x+1])/2)
    for i in range(len(ydatazip)):
        if ydatazip[i] < 0:
            d = i
    uleer = abs((xdatazip[d]+xdatazip[d+1])/2)
    arr = xdatazip[x:d+1] * ydatazip[x:d+1]
    plt.scatter(xdatazip[x:d+1], arr)
    pmax = abs(min(arr))
    sf = uleer/1.12
    ff = pmax/(ifoto*uleer)
    cf = sf * ff
    #print("I_Foto: ", ifoto)
    #print("U_L: ", uleer)
    #print("max Leistung: ", pmax)
    #print("Spannungsfaktor: ", sf)
    #print("Füllfaktor: ", ff)
    #print("cFaktor: ", cf)
    #xlist = np.linspace(min(xdatazip[a:x + b]), max(xdatazip[a:x + b]), 1000)
    #popt, pcov = curve_fit(lambda x, a, b, c: a * (np.exp(x / b) - 1) - c, xdatazip[a:x + b], ydatazip[a:x + b])
    #y = popt[0] * (np.e ** (xlist / popt[1]) - 1) - popt[2]
    #plt.plot(xlist, y, color="red")
    #plt.scatter(xdatazip[a:x + b], ydatazip[a:x + b])
    #print(popt)
    plt.show()
    Name.append(Pfad[0:len(Pfad)-22])
    Fotostrom.append(1000*ifoto)
    Uleer.append(uleer)
    maxLeistung.append(pmax * 1000)
    Spannungsfaktor.append(sf)
    Füllfaktor.append(ff)
    charaktFaktor.append(cf)
#Auswertung("6volt/Grün_525nm_Durchlassrichtung.txt","6volt/Grün_525nm_Sperrrichtung.txt")

def Auswertung2(Pfad):
    data = pd.read_csv(Pfad, sep=",")
    xdata = np.array(data[" U (V)"])
    ydata = np.array(data[" I (A)"])
    ifoto = abs(ydata[0])
    uleer = xdata[len(xdata)-1]
    arr = xdata * ydata
    plt.scatter(xdata, arr)
    pmax = abs(min(arr))
    sf = uleer/1.12
    ff = pmax/(ifoto*uleer)
    cf = sf * ff

    Name.append(Pfad[5:len(Pfad)-4])
    Fotostrom.append(1000*ifoto)
    Uleer.append(uleer)
    maxLeistung.append(pmax*1000)
    Spannungsfaktor.append(sf)
    Füllfaktor.append(ff)
    charaktFaktor.append(cf)
    plt.show()

#Auswertung2("6volt/Grün525nm.txt")
#Auswertung2("6volt/Rot630nm.txt")
#Auswertung2("6volt/WeißesLicht60W.txt")
#Auswertung("6volt/Grün_525nm_Durchlassrichtung.txt", '6volt/Grün_525nm_Sperrrichtung.txt')


Plotter("6volt/Tageslicht-Durchlassrichtung.txt", "6volt/Tageslicht-Sperrrichtung.txt", "Tageslicht", "x", 'tab:blue')
Plotter("6volt/WeißesLicht_60W_Durchlassrichtung.txt", "6volt/WeißesLicht_60W_Sperrrichtung.txt", "Weiß", "D", 'm')
Plotter("6volt/Grün_525nm_Durchlassrichtung.txt", "6volt/Grün_525nm_Sperrrichtung.txt", "Grün", "v", 'tab:green')
Plotter("6volt/Rot_630nm_Durchlassrichtung.txt", "6volt/Rot_630nm_Sperrrichtung.txt", "Rot", "x", 'tab:red')
Plotter("6volt/Dunkelmessung_Durchlassrichtung.txt", "6volt/Dunkelmessung_Sperrrichtung.txt", "Dunkel", ".", 'black')
plt.legend(loc = "upper left" , fancybox = True , frameon = True , edgecolor = "black")
plt.grid()
plt.show()
#fig, ax1 = plt.subplots()
#xdata, ydata = Sperrplotter('6volt/Tageslicht.txt')
#ax1.scatter(xdata, 1000*ydata, color='tab:blue', marker='x', label='Tageslicht')
#xdata, ydata = Sperrplotter('6volt/Grün525nm.txt')
#Sperrplotter('Tageslicht.txt', "Tageslicht", "x", 'tab:blue')#
#ax1.scatter(xdata, 1000*ydata, color='tab:green', marker='v', label='Grün')
#ax1.tick_params(axis='y')
#ax1.set_ylabel('Strom in mA (Rot, Grün, Tageslicht)')
#xdata, ydata = Sperrplotter('6volt/Rot630nm.txt')
#ax1.scatter(xdata, 1000*ydata, color='tab:red', marker='+', label='Rot')
#ax1.grid()
#ax2 = ax1.twinx()
#xdata, ydata = Sperrplotter('6volt/WeißesLicht60W.txt')
#ax2.scatter(xdata, 1000*ydata, color='m', marker='D', label='Weiß')
#ax2.set_ylabel('Strom in mA (Weißes Licht)', color='m')
#ax1.set_xlabel('Spannung in V')
#ax2.tick_params(axis='y', labelcolor='m')
#ax2.scatter([], [], color='tab:blue', marker='x', label='Tageslicht')
#ax2.scatter([], [], color='tab:green', marker='v', label='Grün')
#ax2.scatter([], [], color='tab:red', marker='+', label='Rot')
#Sperrplotter('Tageslicht.txt', "Tageslicht", "x", 'tab:blue')
#Sperrplotter('WeißesLicht60W.txt', "Weiß", "D", 'm')
#Sperrplotter('Grün525nm.txt', "Grün", "v", 'tab:green')
#Sperrplotter('RotesLicht630nm.txt', "Rot", "+", 'tab:red')
#plt.legend(loc = "upper left" , fancybox = True , frameon = True , edgecolor = "black")
#fig.tight_layout()
#plt.show()

#Sperrplotter("Grün_525nm_Sperrrichtung.txt", "Grün", "+")
#Sperrplotter("Rot_630nm_Sperrrichtung.txt", "Rot", "v")
#Sperrplotter("WeißesLicht_60W_Sperrrichtung.txt", "Weiß", "D")
#Sperrplotter("Tageslicht_Sperrrichtung.txt",  "Tageslicht", "x")
#plt.legend(loc = "center left" , fancybox = True , frameon = True , edgecolor = "black")

#plt.show()
# plt.legend(loc = "upper right" , fancybox = True , frameon = True , edgecolor = "black")
#lnPlotter("Grün_525nm_Durchlassrichtung.txt", "Grün_525nm_Sperrrichtung.txt", "Grün", "+")

#plt.legend(loc = "upper left" , fancybox = True , frameon = True , edgecolor = "black")
#plt.grid()
#plt.show()
#plt.scatter(xgreenzip, ygreenzip)
#plt.scatter(xrotzip, yrotzip)
#plt.show()

df = pd.DataFrame({'2V': Name,
                   '$I_\mathrm{Foto}$/mA': Fotostrom,
                  '$U_L$/V': Uleer,
                   '$P_\mathrm{max}$/mW': maxLeistung,
               '$SF$': Spannungsfaktor,
                   '$FF$': Füllfaktor,
                   '$CF$': charaktFaktor})


df = df.style.format(decimal=',', thousands='.', precision=2)
print(df.to_latex())


