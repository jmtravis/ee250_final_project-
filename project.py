import asyncio
import json
from shazamio import Shazam


async def main():
  shazam = Shazam()
  out = await shazam.recognize_song('kokomo.m4a')
  pretty = json.dumps(out, indent=4)
  print(pretty)
  title = out['track']['title']
  artist = out['track']['subtitle']
  print(title)
  print(artist)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())