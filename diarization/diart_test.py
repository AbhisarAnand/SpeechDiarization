from diart import SpeakerDiarization
from diart.sources import MicrophoneAudioSource
from diart.inference import StreamingInference
from diart.sinks import RTTMWriter

pipeline = SpeakerDiarization()
mic = MicrophoneAudioSource()
print(mic.uri)
inference = StreamingInference(pipeline, mic, do_plot=True)
inference.attach_observers(RTTMWriter(mic.uri, "file.rttm"))
prediction = inference()
print(prediction)
