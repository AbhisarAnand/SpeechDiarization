import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load("../diarization/test.wav")
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()
