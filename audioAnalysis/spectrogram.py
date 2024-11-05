import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

y, sr = librosa.load("test_two_people1.wav")
S = librosa.feature.melspectrogram(y=y, sr=sr)
S_dB = librosa.power_to_db(S, ref=np.max)

plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-frequency spectrogram of 2 People Talking')
plt.tight_layout()
plt.show()
