import asyncio
from shazamio import Shazam
import requests
import sys

SERVER = 'http://172.20.10.6:5000'

async def main():
  song = sys.argv[1]
  shazam = Shazam()
  out = await shazam.recognize_song(song)
  print(out)
  response = requests.post(f'{SERVER}/recognize', json=out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())