import socket
import rsa
import pickle

def bob():
    # Generate public and private keys for Bob
    bob_pub, bob_priv = rsa.newkeys(1024)
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))
    
    # Receive Alice's public key
    alice_pub_pem = client_socket.recv(4096)
    alice_pub = rsa.PublicKey.load_pkcs1(alice_pub_pem)
    print("Received Alice's public key.")
    print(f"Alice's public key: PublicKey({alice_pub.n})")
    
    # Send Bob's public key to Alice
    bob_pub_pem = bob_pub.save_pkcs1()
    client_socket.sendall(bob_pub_pem)
    
    while True:
        # Receive encrypted message from Alice
        alice_cipher = client_socket.recv(4096)
        if not alice_cipher:
            break
        print(f"Received encrypted message from Alice: {alice_cipher}")
        alice_msg = rsa.decrypt(alice_cipher, bob_priv).decode('utf-8')
        print(f"Decrypted message from Alice: {alice_msg}")
        
        # Input Alice's message, encrypting the message and sending the message
        bob_msg = input("Enter message for Alice: ").encode('utf-8')
        bob_cipher = rsa.encrypt(bob_msg, alice_pub)
        print(f"Sending encrypted message to Alice: {bob_cipher}")
        client_socket.sendall(bob_cipher)
        
        # Check if Bob wants to end the conversation
        if input("Do you wish to break (y/n): ").lower() == 'y':
            break
    
    client_socket.close()

bob()
