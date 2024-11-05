import threading
import sounddevice as sd
import numpy as np
from diart import SpeakerDiarization
from diart.inference import StreamingInference
from diart.sinks import RTTMWriter
from datetime import datetime, timedelta

class RealTimeDiarizationRecorder:
	def __init__(self):
		self.pipeline = SpeakerDiarization()
		self.transcript = []
		self.recording = False
		self.stream = None

	def start_recording(self):
		"""Start recording audio with real-time diarization."""
		self.recording = True
		self.start_time = datetime.now()
		print("Recording started... Press Enter to stop recording.")

		# Attach an RTTM writer to capture speaker information
		self.rttm_writer = RTTMWriter("mic", "file.rttm")

		# Start the audio stream in a new thread
		self.stream = sd.InputStream(callback=self.audio_callback, channels=1, samplerate=16000)
		self.stream.start()

	def audio_callback(self, indata, frames, time, status):
		"""Callback function for streaming audio input to diarization pipeline."""
		if status:
			print(status)
		if self.recording:
			# Convert audio input to required format for diarization
			audio_chunk = np.frombuffer(indata, dtype=np.float32)
			prediction = self.pipeline(audio_chunk)

			# Process prediction and store transcript
			self.process_prediction(prediction)

	def stop_recording(self):
		"""Stops the audio recording."""
		self.recording = False
		print("Recording stopped.")
		self.stream.stop()
		self.stream.close()
		self.display_transcript()

	def process_prediction(self, prediction):
		"""Processes each prediction segment into readable transcript entries."""
		for segment in prediction.iter_segments():
			timestamp = self.start_time + timedelta(seconds=segment.start)
			speaker_entry = {
				"time": timestamp.strftime("%H:%M:%S"),
				"speaker": segment.track,
				"text": f"Speaker {segment.track} speaking from {segment.start:.2f}s to {segment.end:.2f}s"
			}
			self.transcript.append(speaker_entry)
			print(speaker_entry["text"])

	def display_transcript(self):
		"""Prints the transcript in a readable format."""
		print("\nTranscript:")
		for entry in self.transcript:
			print(f"[{entry['time']}] {entry['text']}")

# Usage
diarization_recorder = RealTimeDiarizationRecorder()

# Start recording
input("Press Enter to start recording...")
diarization_recorder.start_recording()

# Stop recording after user presses Enter again
input("Press Enter to stop recording...")
diarization_recorder.stop_recording()