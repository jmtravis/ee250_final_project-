import asyncio
from shazamio import Shazam
import requests
import pyaudio
import wave
import os

SERVER = 'http://172.20.10.6:5000'

async def main():
  # the file name output you want to record into
  filename = "recording.wav"
  # set the chunk size of 1024 samples
  chunk = 1024
  # sample format
  FORMAT = pyaudio.paInt16
  # mono, change to 2 if you want stereo
  channels = 1
  # 44100 samples per second
  sample_rate = 44100
  record_seconds = 10
  # initialize PyAudio object
  p = pyaudio.PyAudio()
  # open stream object as input & output
  stream = p.open(format=FORMAT,
                  channels=channels,
                  rate=sample_rate,
                  input=True,
                  output=True,
                  frames_per_buffer=chunk)
  frames = []
  signal = input("Press ENTER to start recording.")
  # while signal != "\n":
  #   signal = input("Press ENTER to start recording.")
  print("Recording...")
  for i in range(int(sample_rate / chunk * record_seconds)):
      data = stream.read(chunk, exception_on_overflow = False)
      # if you want to hear your voice while recording
      # stream.write(data)
      frames.append(data)
  print("Finished recording.")
  # stop and close stream
  stream.stop_stream()
  stream.close()
  # terminate pyaudio object
  p.terminate()
  # save audio file
  # open the file in 'write bytes' mode
  wf = wave.open(filename, "wb")
  # set the channels
  wf.setnchannels(channels)
  # set the sample format
  wf.setsampwidth(p.get_sample_size(FORMAT))
  # set the sample rate
  wf.setframerate(sample_rate)
  # write the frames as bytes
  wf.writeframes(b"".join(frames))
  # close the file
  wf.close()
  os.rename(f'{filename}', f'data/{filename}')
  # song = sys.argv[1]
  shazam = Shazam()
  out = await shazam.recognize_song(f'data/{filename}')
  print(out)
  response = requests.post(f'{SERVER}/recognize', json=out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())