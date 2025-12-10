# UDP Escape Room
This project was developed to utilize the User Datagram Protocol in an interesting way. Gather clues from an alarm clock radio to escape the room you've found yourself in. You may need to look up a few things.

This code was written entirely by me. There is no AI code in this project. Gemini Nano Banana Pro was used to create the lock images and alarm clock image. The images were modified after generation.

# UDP Analogy
In the game, the radio tower transmits a message to the alarm clock radio depending on the frequency it has been set to. The UDP client socket sends the frequency value to the UDP server, then a stored "radio transmission" string is served back to the client. 

This analogy is somewhat flawed since a real radio tower does not receive any information from a radio receiver. With that said, the radio transmitter/receiver relationship is far more like UDP than TCP, because a radio transmitter and receiver do not establish and verify a connection prior to exchanging information.

# How to Play
1. Move all project files into a Python project in your preferred IDE.
2. Ensure that the Python packages listed at the top of `tower.py` and `receiver.py` are installed on your system or in your virtual environment.
3. Adjust the `server_ip` variable in the `connection_info()` function to reflect the ip address of the device running `tower.py`.
4. Run `tower.py`, then run `receiver.py`.

# References
Module 5: Transport Layer by [Dr. Pulin Agrawal](https://sites.google.com/view/pulinagrawal)
