'''
3 types of Audio Files
.mp3 // lossy compressions format least audio quality
.flac // lossy less format
.wav // uncompressed format best audio quality

'''

import wave
import numpy as np
import matplotlib.pyplot as plt



# Audio Signal Parameters
# - number of channel (1, mono, 2 audio is coming from 2 diff directions)
# - sample width (no of bytes)
# - sample rate (frequency - no of samples per second)
# - number of frames 
# - value of a frame

audio_obj = wave.open("ishan-audio.wav", "rb")

print(" Channels ", audio_obj.getnchannels())
print(" Width ", audio_obj.getsampwidth())
print(" Rate ", audio_obj.getframerate())
print(" Frames ", audio_obj.getnframes())
print(" Frame Value ", audio_obj.getnframes())

time_of_audio = audio_obj.getnframes() / audio_obj.getframerate()
samples = audio_obj.getnframes()
print(" Time of Audio is ", time_of_audio)


'''
Plot the Audio
'''

obj = wave.open("ishan-audio.wav")
sample_freq = obj.getframerate()
n_sample = obj.getnframes()
signal_wave = audio_obj.readframes(-1)
obj.close()

t_audio = int(n_sample/sample_freq)

print(t_audio)

plt.figure(figsize=(15, 5))
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
times = np.linspace(0, t_audio, num =sample_freq )

print(times.shape, signal_array.shape)
times_truncated = signal_array[:len(times)]

plt.plot(times_truncated)
plt.show()

