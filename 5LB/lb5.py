import hashlib
import base64
import os

def generate_key(full_name, birth_year):
    seed = f"{full_name}{birth_year}"
    return hashlib.sha256(seed.encode('utf-8')).digest()

def encrypt_message(message, key):
    msg_bytes = message.encode('utf-8')
    encrypted_bytes = bytearray()
    for i in range(len(msg_bytes)):
        encrypted_bytes.append(msg_bytes[i] ^ key[i % len(key)])
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt_message(encrypted_b64, key):
    encrypted_bytes = base64.b64decode(encrypted_b64)
    decrypted_bytes = bytearray()
    for i in range(len(encrypted_bytes)):
        decrypted_bytes.append(encrypted_bytes[i] ^ key[i % len(key)])
    return decrypted_bytes.decode('utf-8')

user_email = "shovheniuk.oleksandr@hneu.net"
user_name = "Oleksandr Shovheniuk"
user_year = "2004"

key = generate_key(user_name, user_year)

print(f"--- СИСТЕМА ЗАХИЩЕНОЇ ПОШТИ ---")
print(f"Користувач: {user_name} ({user_email})")
print(f"Ключ активовано: {key.hex()[:16]}...\n")

user_input = input("Введіть текст повідомлення для шифрування: ")

if user_input:
    encrypted = encrypt_message(user_input, key)
    print(f"\n[ВІДПРАВКА]")
    print(f"Зашифрований блок (Base64):")
    print(f"-----BEGIN PROTECTED MESSAGE-----")
    print(encrypted)
    print(f"-----END PROTECTED MESSAGE-----\n")

    print(f"[ОТРИМАННЯ]")
    decrypted = decrypt_message(encrypted, key)
    print(f"Розшифрований текст: {decrypted}")
else:
    print("Повідомлення не введено.")