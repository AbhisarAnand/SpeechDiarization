import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load("../diarization/test.wav")
chroma = librosa.feature.chroma_stft(y=y, sr=sr)

plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', cmap='coolwarm')
plt.colorbar()
plt.title('Chroma Features')
plt.show()
