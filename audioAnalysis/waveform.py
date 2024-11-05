import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load("test.wav")
plt.figure()
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.show()

