# AudioRecorder.py
import sounddevice as sd
import soundfile as sf

class AudioRecorder:
    def __init__(self, samplerate=44100, channels=1):
        self.samplerate = samplerate
        self.channels = channels

    def list_devices(self):
        """List all available audio devices and their information."""
        print(sd.query_devices())

    def record_audio(self, duration, filename):
        """Record audio from the microphone and save it as a WAV file."""
        print(f"Recording for {duration} seconds...")
        audio = sd.rec(int(self.samplerate * duration), samplerate=self.samplerate, channels=self.channels, dtype='float32')
        sd.wait()  # Wait until recording is finished
        sf.write(filename, audio, self.samplerate)
        print(f"Recording saved as {filename}")
    
    def remove_audio(self, filename):
        """Remove the audio file."""
        import os
        os.remove(filename)
        print(f"Removed {filename}")


if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.list_devices()
    recorder.record_audio(10, "test_two_people.wav")
    # recorder.remove_audio("test.wav")
