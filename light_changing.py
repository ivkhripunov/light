import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    background = photo[455:855, 900:1090, 0:3].swapaxes(0, 1)

    cut = photo[455:855, 910:1070, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()

    plt.imshow(background, origin='lower')

    plt.savefig(plotName)

    return luma

def giveIntencity(photoName):
    photo = imageio.imread(photoName)
    background = photo[455:855, 900:1090, 0:3].swapaxes(0, 1)

    cut = photo[455:855, 910:1070, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    return luma


#readIntensity("E:\общеинженерная подготовка\лабораторная 3\data\\blue.jpeg", "E:\общеинженерная подготовка\лабораторная 3\plots\\blue - list.jpeg", "Лампа накаливания", "Синий лист")

valswh = giveIntencity("E:\общеинженерная подготовка\лабораторная 3\data\white.jpeg")
valswh = np.array(valswh)
srwh = 1

valsgr = giveIntencity("E:\общеинженерная подготовка\лабораторная 3\data\green2.jpeg")
valsgr = np.array(valsgr)
srgr = 0
for i in range(len(valswh)):
    valsgr[i] = valsgr[i] / (valswh[i] + 1)
    srgr += valsgr[i]
srgr = srgr / len(valswh)

valsred = giveIntencity("E:\общеинженерная подготовка\лабораторная 3\data\ired.jpeg")
valsred = np.array(valsred)
srred = 0
for i in range(len(valswh)):
    valsred[i] = valsred[i] / (valswh[i] + 1)
    srred += valsred[i]
srred = srgr / len(valswh)

valsblue = giveIntencity("E:\общеинженерная подготовка\лабораторная 3\data\\blue.jpeg")
valsblue = np.array(valsblue)
srblue = 0
for i in range(len(valswh)):
    valsblue[i] = valsblue[i] / (valswh[i] + 1)
    srblue += valsblue[i]
srblue = srblue / len(valswh)

valsye = giveIntencity("E:\общеинженерная подготовка\лабораторная 3\data\yellow.jpeg")
valsye = np.array(valsye)
srye = 0
for i in range(len(valswh)):
    valsye[i] = valsye[i] / (valswh[i] + 1)
    srye += valsye[i]
srye = srye / len(valswh)


lengths = []
for i in range(len(valswh)):
    lengths.append(669 - 0.8 * i)

for i in range(len(valswh)):
    valswh[i] = 1

fig, ax = plt.subplots(figsize=(12, 9))
ax.plot(lengths, valswh,
        linestyle='-',
        linewidth=1,
        # markevery=markers_on,
        color='darkmagenta')
ax.plot(lengths, valsred,
        linestyle='-',
        linewidth=1,
        # markevery=markers_on,
        color='r')
ax.plot(lengths, valsgr,
        linestyle='-',
        linewidth=1,
        # markevery=markers_on,
        color='g')
ax.plot(lengths, valsblue,
        linestyle='-',
        linewidth=1,
        # markevery=markers_on,
        color='b')
ax.plot(lengths, valsye,
        linestyle='-',
        linewidth=1,
        # markevery=markers_on,
        color='orange')

ax.set_title('Альбедо поверхностей', style='italic')
ax.legend(labels=("Белый лист - 1","красный лист - 0.7","зелёный лист - 0.45","синий лист - 0.35"
                  ,"жёлтый лист - 0.85","Q (50мм) = 6.43 (г/с)" ,"Q (60мм) = 6.66 (г/с)" ,"Q (70мм) = 7.69 (г/с)"), loc="upper left")
ax.set_ylabel('Альбедо')
ax.set_xlabel('длина волны (нм)')
# ax.figure(figsize=(10, 7))
ax.axes.grid(
    which="major",
    linewidth="0.4",
   )
ax.minorticks_on()
ax.axes.grid(
        which="minor",
        linewidth="0.2"
    )


plt.show()
