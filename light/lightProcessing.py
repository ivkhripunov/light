import numpy as np
import matplotlib.pyplot as plt
from lightFunctions import readIntensity
import math

calibrationArray = readIntensity("light/data/white-mercury.png", "light/plots/white-mercury.png", "ртутная лампа", "белый лист")

blueArray = readIntensity("light/data/blue-tungsten.png", "light/plots/blue-tungsten.png", "лампа накаливания", "синий лист")
redArray = readIntensity("light/data/red-tungsten.png", "light/plots/red-tungsten.png", "лампа накаливания", "красный лист")
yellowArray = readIntensity("light/data/yellow-tungsten.png", "light/plots/yellow-tungsten.png", "лампа накаливания", "жёлтый лист")
greenArray = readIntensity("light/data/green-tungsten.png", "light/plots/green-tungsten.png", "лампа накаливания", "зелёный лист")
whiteArray = readIntensity("light/data/white-tungsten.png", "light/plots/white-tungsten.png", "лампа накаливания", "белый лист")

redPike = np.argmax(calibrationArray)
for i in range (redPike - 20, redPike + 20):
    calibrationArray[i] = 0
greenPike = np.argmax(calibrationArray)

refRedPike = 610.0
refGreenPike = 545.0
length = (650 * (refRedPike - refGreenPike))/(redPike - greenPike)
maxLength = (greenPike * length)/650 + refGreenPike
minLength = refGreenPike - (greenPike * length)/650
maxX = math.ceil(maxLength / 20.0) * 20
minX = math.floor(minLength / 20.0) * 20
maxIntensity = max(np.amax(whiteArray), np.amax(blueArray), np.amax(redArray), np.amax(yellowArray), np.amax(greenArray))
maxY = math.ceil(maxIntensity / 10.0) * 10
minY = -7
waveLengthArray = np.arange(minLength, maxLength, (maxLength - minLength)/calibrationArray.size)

fig = plt.figure(figsize=(16, 10), dpi=400)
ax = plt.axes()
ax.set(facecolor = "#c8c8c9")

plt.plot(waveLengthArray, blueArray, '#0000ff', label='синий лист', linewidth = 3)
plt.plot(waveLengthArray, redArray, '#ff0000', label='красный лист', linewidth = 3)
plt.plot(waveLengthArray, yellowArray, '#feff00', label='жёлтый лист', linewidth = 3)
plt.plot(waveLengthArray, greenArray, '#00ff00', label='зелёный лист', linewidth = 3)
plt.plot(waveLengthArray, whiteArray, '#ffffff', label='белый лист', linewidth = 3)

plt.xlim(minX, maxX)
plt.ylim(minY, maxY)

plt.xticks(np.arange(350, maxX, 50), fontsize = 16)
plt.yticks(np.arange(0, maxY, 10), fontsize = 16)
ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))

ax.grid(which = 'major', c = '#696969', linestyle = '-', linewidth = 2, alpha = 0.6)
ax.grid(which = 'minor', c = '#696969', linestyle = '--', linewidth = 1, alpha = 0.6)

plt.title('Интенсивность отражённого излучения', loc = 'center', fontsize = 24, wrap = True)
plt.xlabel('Длина волны [нм]', fontsize = 18)
plt.ylabel('Яркость', fontsize = 18)
plt.legend(fontsize = 14)

plt.savefig("light/plots/intensites.png")



fig = plt.figure(figsize=(16, 10), dpi=400)
ax = plt.axes()
ax.set(facecolor = "#c8c8c9")

ones = np.ones(whiteArray.size, dtype=float)
whiteArray = whiteArray + ones

blueAlbedoArray = blueArray/whiteArray
redAlbedoArray = redArray/whiteArray
yellowAlbedoArray = yellowArray/whiteArray
greenAlbedoArray = greenArray/whiteArray
whiteAlbedoArray = whiteArray/whiteArray
maxY = 1.75
minY = -0.25

plt.plot(waveLengthArray, blueAlbedoArray, '#0000ff', label='синий лист', linewidth = 3)
plt.plot(waveLengthArray, redAlbedoArray, '#ff0000', label='красный лист', linewidth = 3)
plt.plot(waveLengthArray, yellowAlbedoArray, '#feff00', label='жёлтый лист', linewidth = 3)
plt.plot(waveLengthArray, greenAlbedoArray, '#00ff00', label='зелёный лист', linewidth = 3)
plt.plot(waveLengthArray, whiteAlbedoArray, '#ffffff', label='белый лист', linewidth = 3)

plt.xlim(minX, maxX)
plt.ylim(minY, maxY)

plt.xticks(np.arange(350, maxX, 50), fontsize = 16)
plt.yticks(np.arange(0, maxY, 0.25), fontsize = 16)
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))

ax.grid(which = 'major', c = '#696969', linestyle = '-', linewidth = 2, alpha = 0.6)
ax.grid(which = 'minor', c = '#696969', linestyle = '--', linewidth = 1, alpha = 0.6)

plt.title('Интенсивность отражённого излучения', loc = 'center', fontsize = 24, wrap = True)
plt.xlabel('Длина волны [нм]', fontsize = 18)
plt.ylabel('Яркость', fontsize = 18)
plt.legend(fontsize = 14)

plt.savefig("light/plots/albedos.png")