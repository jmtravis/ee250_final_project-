import asyncio
from shazamio import Shazam
import requests

SERVER = 'http://172.20.10.6:5000'

async def main():
  shazam = Shazam()
  out = await shazam.recognize_song('dojacat.m4a')
  print(out)
  response = requests.post(f'{SERVER}/recognize', json=out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())