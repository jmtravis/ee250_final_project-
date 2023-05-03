import asyncio
from shazamio import Shazam
import requests

SERVER = 'http://localhost:5000'

async def main():
  shazam = Shazam()
  out = await shazam.recognize_song('kokomo.m4a')
  response = requests.post(f'{SERVER}/recognize', json=out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())