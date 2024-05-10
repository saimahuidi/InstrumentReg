import torchaudio

waveform, sample_rate = torchaudio.load('dataset/')
print(f"The sample rate is: {sample_rate}")
