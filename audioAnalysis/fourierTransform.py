import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import librosa

y, sr = librosa.load("../diarization/test.wav")
n = len(y)
T = 1.0 / sr
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), n//2)

plt.plot(xf, 2.0/n * np.abs(yf[:n//2]))
plt.grid()
plt.title('FFT - Frequency Spectrum')
plt.show()