RSA Secure Chat


A simple Python-based encrypted chat system between two users — Alice and Bob — built using RSA encryption and socket programming. This project demonstrates how public-key cryptography can be used to secure real-time communication between two endpoints.


A simple Python-based encrypted chat system between two users — Alice and Bob — built using RSA encryption and socket programming. This project demonstrates how public-key cryptography can be used to secure real-time communication between two endpoints.

Features
•	Secure two-way chat using RSA public and private keys
•	Real-time communication via TCP sockets
•	Demonstrates encryption and decryption in Python
•	Simple command-line interface for learning purposes
•	Easy to set up and run locally



Technologies Used
•	Python 3
•	rsa library
•	socket library
•	pickle for serialization

How It Works
1.	Alice (Server) starts first and waits for a connection.
2.	Bob (Client) connects to Alice.
3.	Both exchange public keys securely.
4.	Messages are encrypted and decrypted using RSA keys.
5.	Ensures secure communication even if intercepted.
<<<<<<< HEAD


Setup Instructions
1. Install Python dependencies:
   pip install rsa
2. Run the programs:
   python alice.py (server)
   python bob.py (client)
3. Start chatting — messages are encrypted and decrypted automatically.

Project Structure

rsa-secure-chat/
├── alice.py         # Server-side script (Alice)
├── bob.py           # Client-side script (Bob)
├── .gitignore       # Git ignore file for sensitive/unnecessary files
└── README.md        # Project documentation


