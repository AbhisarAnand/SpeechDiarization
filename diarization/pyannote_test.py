from pyannote.audio import Pipeline

# Load the pre-trained diarization pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token="")

# Apply diarization on your audio file
diarization = pipeline("test2people.wav")

# Display diarization results
for turn, _, speaker in diarization.itertracks(yield_label=True):
	print(f"{turn.start:.1f}s - {turn.end:.1f}s: speaker {speaker}")
