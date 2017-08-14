# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:22:44 2017

@author: David Quintero Montoya
"""
import numpy as np
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import zero_crossing as zerocr

# Datos en dBares
RBR_Caso_1 = np.loadtxt("RBR_burst_4_Caso_1.txt",skiprows = 1) 
RBR_Caso_2 = np.loadtxt("RBR_burst_5_Caso_2.txt",skiprows = 1) 
RBR_Caso_3 = np.loadtxt("RBR_burst_6_Caso_3.txt",skiprows = 1) 
RBR_Caso_4 = np.loadtxt("RBR_burst_7_Caso_4.txt",skiprows = 1) 
RBR_Caso_5 = np.loadtxt("RBR_burst_8_Caso_5.txt",skiprows = 1) 
RBR_Caso_6 = np.loadtxt("RBR_burst_9_Caso_6.txt",skiprows = 1) 

#Datos en Bares
BlueLog_Caso_1 = np.loadtxt("BlueLog_burst_10_Caso_1.txt",skiprows = 1) 
BlueLog_Caso_2 = np.loadtxt("BlueLog_burst_11_Caso_2.txt",skiprows = 1) 
BlueLog_Caso_3 = np.loadtxt("BlueLog_burst_12_Caso_3.txt",skiprows = 1) 
BlueLog_Caso_4 = np.loadtxt("BlueLog_burst_13_Caso_4.txt",skiprows = 1) 
BlueLog_Caso_5 = np.loadtxt("BlueLog_burst_14_Caso_5.txt",skiprows = 1) 
BlueLog_Caso_6 = np.loadtxt("BlueLog_burst_15_Caso_6.txt",skiprows = 1) 
#Conversion a dBares
BlueLog_Caso_1_dBares= 10 * BlueLog_Caso_1
BlueLog_Caso_2_dBares= 10 * BlueLog_Caso_2
BlueLog_Caso_3_dBares= 10 * BlueLog_Caso_3
BlueLog_Caso_4_dBares= 10 * BlueLog_Caso_4
BlueLog_Caso_5_dBares= 10 * BlueLog_Caso_5
BlueLog_Caso_6_dBares= 10 * BlueLog_Caso_6

#correccion por altura de los sensores
atm=8.5 #en dBar
ajust = ((RBR_Caso_2[1]-atm)-(BlueLog_Caso_2_dBares[1]-atm))
BlueLog_Caso_1_dBares= ajust+ BlueLog_Caso_1_dBares
BlueLog_Caso_2_dBares= ajust+ BlueLog_Caso_2_dBares
BlueLog_Caso_3_dBares= ajust+ BlueLog_Caso_3_dBares
BlueLog_Caso_4_dBares= ajust+ BlueLog_Caso_4_dBares
BlueLog_Caso_5_dBares= ajust+ BlueLog_Caso_5_dBares
BlueLog_Caso_6_dBares= ajust+ BlueLog_Caso_6_dBares


#Linea de tiempo para graficar (eje temporal x=tiempo)
#X = np.linspace(0,341.3,2048, endpoint=True)
X = np.linspace(0,2048,2048, endpoint=True)

#graficas 1
plt.figure(1)
plt.plot(X,RBR_Caso_1,color ='green', linewidth=1.5, linestyle="-")
plt.plot(X,BlueLog_Caso_1_dBares,color ='blue', linewidth=1.5, linestyle="-")
#leyenda
green_line = mlines.Line2D([], [], color='green', marker='_', markersize=15, label='RBR')
blue_line = mlines.Line2D([], [], color='blue', marker='_', markersize=15, label='BlueLog')
plt.legend(handles=[blue_line,green_line])
#imprimimos las graficas
plt.show()

#graficas 2
plt.figure(2)
plt.plot(X,RBR_Caso_2,color ='green', linewidth=1.5, linestyle="-")
plt.plot(X,BlueLog_Caso_2_dBares,color ='blue', linewidth=1.5, linestyle="-")
#leyenda
green_line = mlines.Line2D([], [], color='green', marker='_', markersize=15, label='RBR')
blue_line = mlines.Line2D([], [], color='blue', marker='_', markersize=15, label='BlueLog')
plt.legend(handles=[blue_line,green_line])
#imprimimos las graficas
plt.show()

#graficas 2
plt.figure(6)
plt.plot(X,RBR_Caso_6,color ='green', linewidth=1.5, linestyle="-")
plt.plot(X,BlueLog_Caso_6_dBares,color ='blue', linewidth=1.5, linestyle="-")
#leyenda
green_line = mlines.Line2D([], [], color='green', marker='_', markersize=15, label='RBR')
blue_line = mlines.Line2D([], [], color='blue', marker='_', markersize=15, label='BlueLog')
plt.legend(handles=[blue_line,green_line])
#imprimimos las graficas
plt.show()

mean = np.mean(RBR_Caso_6)
serie = RBR_Caso_6-mean
zerocr.zero_crossing(X,serie)