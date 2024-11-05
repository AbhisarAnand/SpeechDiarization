import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load("test_two_people1.wav")
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC for 2 People Talking')
plt.tight_layout()
plt.show()
