'''
3 types of Audio Files
.mp3 // lossy compressions format least audio quality
.flac // lossy less format
.wav // uncompressed format best audio quality

'''

import wave
import numpy


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

print(" Time of Audio is ", time_of_audio)

# /Users/ishananand/Desktop/speech_recognition/.venv/bin/python -m pip install matplotlib numpy