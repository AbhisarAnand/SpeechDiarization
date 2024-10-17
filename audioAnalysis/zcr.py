import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load("../diarization/test.wav")
zero_crossings = librosa.zero_crossings(y, pad=False)

plt.figure()
plt.plot(y)
plt.title(f'Zero-Crossing Rate: {sum(zero_crossings)}')
plt.show()
