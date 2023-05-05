# Client runs locally on computer

import asyncio
from shazamio import Shazam
import requests
import pyaudio
import wave
import os

# This was the hostname of our RPi. Change this accordingly.
SERVER = 'http://172.20.10.6:5000'

async def main():
  # The file name output you want to record into
  filename = "recording.wav"
  # Set the chunk size of 1024 samples
  chunk = 1024
  # Sample format
  FORMAT = pyaudio.paInt16
  # Mono, change to 2 if you want stereo
  channels = 1
  # 44100 samples per second
  sample_rate = 44100
  record_seconds = 10
  # Initialize PyAudio object
  p = pyaudio.PyAudio()
  # Open stream object as input & output
  stream = p.open(format=FORMAT,
                  channels=channels,
                  rate=sample_rate,
                  input=True,
                  output=True,
                  frames_per_buffer=chunk)
  frames = []
  # Wait for user input before beginning recording
  signal = input("Press ENTER to start recording.")
  print("Recording...")
  # Read the audio input at consistent intervals over the course of 10 seconds
  for i in range(int(sample_rate / chunk * record_seconds)):
      data = stream.read(chunk, exception_on_overflow = False)
      frames.append(data)
  print("Finished recording.")
  # Stop recording and close stream
  stream.stop_stream()
  stream.close()
  # Terminate pyaudio object
  p.terminate()
  # Save audio file
  # Open the file in 'write bytes' mode
  wf = wave.open(filename, "wb")
  # Set the channels
  wf.setnchannels(channels)
  # Set the sample format
  wf.setsampwidth(p.get_sample_size(FORMAT))
  # Set the sample rate
  wf.setframerate(sample_rate)
  # Write the frames as bytes
  wf.writeframes(b"".join(frames))
  # Close the file
  wf.close()
  # Move the audio file to a data folder, for organizational purposes
  os.rename(f'{filename}', f'data/{filename}')
  # Use the audio file as input for the Shazam API, and store the outputted JSON in a variable
  shazam = Shazam()
  out = await shazam.recognize_song(f'data/{filename}')
  print(out)
  # Make a POST request to the server with the JSON received from the Shazam API
  response = requests.post(f'{SERVER}/recognize', json=out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
