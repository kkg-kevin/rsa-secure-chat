import socket
import rsa
import pickle

def alice():
    # Generate public and private keys for Alice
    alice_pub, alice_priv = rsa.newkeys(1024)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    
    print("Alice is waiting for connection...")
    connection, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
    
    # Send Alice's public key to Bob
    alice_pub_pem = alice_pub.save_pkcs1()
    connection.sendall(alice_pub_pem)
    
    # Receive Bob's public key
    bob_pub_pem = connection.recv(4096)
    bob_pub = rsa.PublicKey.load_pkcs1(bob_pub_pem)
    print("Received Bob's public key.")
    print(f"Bob's public key: PublicKey({bob_pub.n})")

    while True:
        # Input Bob's message, encrypting the message and sending the message
        alice_msg = input("Enter message for Bob: ").encode('utf-8')
        alice_cipher = rsa.encrypt(alice_msg, bob_pub)
        print(f"Sending encrypted message to Bob: {alice_cipher}")
        connection.sendall(alice_cipher)
        
        # Receive encrypted message from Bob
        bob_cipher = connection.recv(4096)
        if not bob_cipher:
            break
        print(f"Received encrypted message from Bob: {bob_cipher}")
        bob_msg = rsa.decrypt(bob_cipher, alice_priv).decode('utf-8')
        print(f"Decrypted message from Bob: {bob_msg}")
        
        # Check if Alice wants to end the conversation
        if input("Do you wish to break (y/n): ").lower() == 'y':
            break
    
    connection.close()
    server_socket.close()

alice()
