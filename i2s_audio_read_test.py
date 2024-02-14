import sounddevice as sd
import numpy as np
import wave

audio_buffer = None

def audio_callback( sddata, data, time, status):
	global audio_buffer
	audio_data = sddata.copy()
	audio_data = audio_data[:, 1]
	if audio_buffer is None:
		audio_buffer = audio_data
	else:
		audio_buffer = np.concatenate((audio_buffer, audio_data))

def  read_audio_from_i2s(duration=20, samplerate=16000, channels=2):
	global audio_buffer
	print("Devices ", sd.query_devices() )
	with sd.InputStream(device=2, callback=audio_callback, dtype='int32', samplerate=samplerate, channels=2):
		sd.sleep(duration*1000)
	save_to_wav("test.wav", audio_buffer, samplerate)


def save_to_wav(filename, data, samplerate):
	with wave.open(filename, 'wb') as wf:
		wf.setnchannels(1)
		wf.setsampwidth(4)
		print("Data Shape ", data.shape, data.dtype )
		wf.setframerate(samplerate)
		print("Shape ", data.shape)
		wf.writeframes(data.tobytes())

if __name__ == "__main__":
	read_audio_from_i2s()
