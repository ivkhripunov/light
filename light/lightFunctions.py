import numpy as np
import matplotlib.pyplot as plt
import imageio

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    cut = photo[400:1050, 1130:1290, 0:3].swapaxes(0, 1)
    intensity = np.mean(cut, axis=(2, 0))

    fig = plt.figure(figsize=(10, 3), dpi=200)
    plt.plot(intensity, 'w', label='{} / {}'.format(lamp, surface))
    plt.imshow(cut, origin='lower')
    plt.title('Интенсивность отражённого излучения')
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')
    plt.legend()
    plt.savefig(plotName)

    return intensity

readIntensity('/home/gr106/Downloads/light-main/scripts/hg1.jpeg', 'График', 'Ртутная лампа', 'white')