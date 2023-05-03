General idea:

1. Collect audio file
2. Receive song title/artist from ShazamIO
        - Data collection
        - Data processing?? (taking JSON file and parsing it for song title/artist. does this count?)
3. Make a POST request to a server running on the RPi, with the song title/artist as the data (or alternatively, the whole JSON could be sent and processing could happen on the RPi)
        - 2+ physical nodes
        - Node-to-node communication
4. The RPi must process the data, and display the song title/artist on an LCD
        - Visualization element