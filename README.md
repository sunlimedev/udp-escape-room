# UDP Escape Room
This project was developed to utilize the User Datagram Protocol in an interesting way. Gather clues from an alarm clock radio to escape the room you've found yourself in. You may need to look up a few things.

This code was written entirely by me. There is no AI code in this project. Gemini Nano Banana Pro was used to create the lock images and alarm clock image. The images were modified after generation.

# UDP Analogy
In the game, the radio tower transmits a message to the alarm clock radio depending on the frequency it has been set to. The UDP client socket sends the frequency value to the UDP server, then a stored "radio transmission" string is served back to the client. 

This analogy is somewhat flawed since a real radio tower does not receive any information from a radio receiver. With that said, the radio transmitter/receiver relationship is far more like UDP than TCP, because a radio transmitter and receiver do not establish and verify a connection prior to exchanging information.

# How to Play
1. Move all project files into a project folder.
2. Ensure that the Python packages listed at the top of `tower.py` and `receiver.py` are installed on your system or in your virtual environment.
3. Adjust the `server_ip` variable in the `connection_info()` function to reflect the ip address of the device running `tower.py`.
4. Run `tower.py`, then run `receiver.py`.

# Spoilers
<details><summary>If you find the escape room to be too difficult you can read the explanation below:</summary>

### The lock requires **three** numbers to open. By tuning the radio to the following frequencies, you will hear these transmissions:<br>

**91.0:** *wish you a happy birthday! Just for you, from Taylor Swift's album, Red, it's*<br>

- When reading the tracklist for Taylor Swift's *Red*, there is a single number: 22. It is implied to be the caller's birthday from the radio transmission, and the station is playing this song for them. This is the first radio trasmission with a clue on the tunable frequency band, thus it is the first number to open the lock.<br>

**93.5:** *not as good as the top song of 19*<br>

- This clue does not have any outside reference. It is implied that the radio station is playing popular songs from a few decades ago. The trasmission is cutoff before the full year is specified, stopping at 19. This is the second radio trasmission with a clue on the tunable frequency band, thus it is the second number to open the lock.<br>

**99.0:** *and that was De La Soul's, The Magic Number. Next up is*<br>

- De La Soul's *The Magic Number* is a song about the number 3. Playing the song will reveal this immediately. This is the third radio trasmission with a clue on the tunable frequency band, thus it is the third number to open the lock.<br>

After visiting these frequencies, the locked can be opened with the sequence: 22-19-3.

</details>

# References
Module 5: Transport Layer by [Dr. Pulin Agrawal](https://sites.google.com/view/pulinagrawal)

[Python Documentation](https://docs.python.org/3/)
