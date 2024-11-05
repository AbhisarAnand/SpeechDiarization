import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load("test_two_people1.wav")
zero_crossings = librosa.zero_crossings(y, pad=False)

plt.figure()
plt.plot(y)
plt.title(f'Zero-Crossing Rate of 2 people talking: {sum(zero_crossings)}')
plt.show()
