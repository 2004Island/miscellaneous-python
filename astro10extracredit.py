from matplotlib import pyplot as plt
import numpy as np

useryear = int(input("What year do you want to see (since 2010) the population and temperature increase?: "))
userssp = int(input("Type in which SSP (1-5) you would like to see: "))

SSP1P = [6.92, 7.79, 8.06, 8.39, 8.53, 8.49, 8.3, 7.97, 7.51, 6.96]
SSP2P = [6.92, 7.79, 8.26, 8.79, 9.17, 9.39, 9.46, 9.41, 9.25, 9.03]
SSP3P = [6.92, 7.79, 8.51, 9.26, 9.96, 10.57, 11.12, 11.63, 12.17, 12.62]
SSP4P = [6.92, 7.79, 8.26, 8.77, 9.15, 9.38, 9.47, 9.48, 9.4, 9.29]
SSP5P = [6.92, 7.79, 8.05, 8.4, 8.58, 8.59, 8.46, 8.2, 7.83, 7.38]

SSPMP = [SSP1P, SSP2P, SSP3P, SSP4P, SSP5P]

SSP1T = [.99, 1.2, 1.49, 1.82, 2.02, 2.25, 2.47, 2.68, 2.87, 3.03]
SSP2T = [.99, 1.2, 1.48, 1.76, 2.12, 2.35, 2.67, 3.02, 3.38, 3.75]
SSP3T = [.99, 1.2, 1.56, 1.88, 2.3, 2.47, 2.79, 3.13, 3.48, 3.85]
SSP4T = [.99, 1.2, 1.51, 1.84, 2.2, 2.44, 2.87, 3.2, 3.49, 3.76]
SSP5T = [.99, 1.2, 1.62, 2.04, 2.4, 2.85, 3.36, 3.88, 4.27, 4.85]

SSPMT = [SSP1T, SSP2T, SSP3T, SSP4T, SSP5T]

def outputgraphcoords(ypv, ssp):
    for i in range(len(ssp)-1):
        for x in np.arange(ssp[i], ssp[i+1], ((ssp[i+1] - ssp[i])/10)):
            ypv.append(round(x,3))

xpv = [i for i in range(2010, 2100)]
populationvectors = [[], [], [], [], []]
temperaturevectors = [[], [], [], [], []]

[outputgraphcoords(populationvectors[i], SSPMP[i]) for i in range(5)]
[outputgraphcoords(temperaturevectors[i], SSPMT[i]) for i in range(5)]

fig, (ax1, ax2) = plt.subplots(1,2)

#[ax1.plot(xpv, populationvectors[i]) for i in range(4)]
#[ax2.plot(xpv, temperaturevectors[i]) for i in range(4)]

ax1.plot(xpv[:(useryear-2010)], populationvectors[userssp-1][:(useryear-2010)], 'r')
ax1.plot(xpv[(useryear-2010):], populationvectors[userssp-1][(useryear-2010):], 'r--')
ax1.annotate(str(int(populationvectors[userssp-1][(useryear-2010)])), (xpv[(useryear-2010)],populationvectors[userssp-1][(useryear-2010)]), textcoords="offset points", xytext=(10,0), ha='center')

ax2.plot(xpv[:(useryear-2010)], temperaturevectors[userssp-1][:(useryear-2010)], 'b')
ax2.plot(xpv[(useryear-2010):], temperaturevectors[userssp-1][(useryear-2010):], 'b--')
ax2.annotate(str(temperaturevectors[userssp-1][(useryear-2010)]), (xpv[(useryear-2010)],temperaturevectors[userssp-1][(useryear-2010)]), textcoords="offset points", xytext=(10,0), ha='center')


ax1.set_title('Population in Billions')
ax2.set_title('Degrees C warming since 1750')
ax1.set(xlabel='year')
ax2.set(xlabel='year')

print(f'There will be {int(populationvectors[userssp-1][(useryear-2010)])} billion people in {xpv[(useryear-2010)]} and the temperature will have risen by {temperaturevectors[userssp-1][(useryear-2010)]}C compared to pre-industrial times')

plt.show()
