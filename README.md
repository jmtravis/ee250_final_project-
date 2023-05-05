# EE 250 Final Project: ShazamPi

# Team Members:
* Jaya Travis 
* Jeremy Pogue 

# Steps for ShazamPi Setup

1. Start RPi with GrovePi LCD attachment and run project_server.py to host the server.
2. Run project_client.py on local computer and press "ENTER" when prompted to start recording the song 
3. Play recording of the song next to computer microphone.
4. Recording will last for 10 seconds then store the audio file to a data file that will be processed by the Shazam API.
5. The server will return the song title and artist(s) name to GrovePi LCD from the JSON data in the client program.
6. Restart client program to continue finding song titles and artist's names!

General Ideas Used for Project: 
* Receive song title/artist from ShazamIO
        - Data collection by recording on local computer.
        - Data processing: take JSON file and parsing it for song title/artist through Shazam API.
 * Make a POST request to a server running on the RPi, with the song title/artist as the data (or alternatively, the whole JSON could be sent and processing could happen on the RPi)
        - 2+ physical nodes : Local computer and RPi
        - Node-to-node communication
* The RPi must process the data, and display the song title/artist on an LCD
        - Visualization element: LCD


# Demonstration Video of Project:

[![ShazamPi Demonstration](http://i.imgur.com/Ot5DWAW.png)](https://youtu.be/rdc01AEyDng "Everything Is AWESOME")

