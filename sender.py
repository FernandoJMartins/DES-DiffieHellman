from diffie_hellman import DiffieHellman
from des import DES
import socket

host = 'localhost'
port = 7070

baseg = 5
primo = 972633691296

sender = DiffieHellman(baseg, primo)  # Cliente

print("============================================ DES WITH DIFFIE HELLMAN ============================================")

# Criando socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:


    client_socket.connect((host, port))
    print("Conectando ", host, ":", port)

    # Envia a chave pública do sender para o receiver
    client_socket.sendall(str(sender.public_key).encode())
    print(f"Chave pública do sender: {sender.public_key}")

    # Recebe a chave pública do receiver
    receiver_public_key = int(client_socket.recv(1024).decode())
    print(f"Chave pública do receiver: {receiver_public_key}")

    # Calcula a chave compartilhada
    shared_key = str(sender.generate_shared_key(receiver_public_key))[:8]  # Ajusta para 8 bytes
    print(f"Chave compartilhada gerada: {shared_key}")

    # Utiliza a chave comum Diffie-Hellman como a chave do DES
    des = DES(shared_key)
    
    # Enviar mensagem criptografada
    message = input("Enviar mensagem: ")
    encrypted_msg = des.encrypt(message)
    client_socket.sendall(encrypted_msg.encode())
    
    print(f"Voce enviou a mensagem criptografada: {encrypted_msg}")
