from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as file:
        file.write(iv + ciphertext)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        data = file.read()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext

def main():
    password = input("Enter password: ")
    salt = os.urandom(16)
    key = generate_key(password, salt)

    choice = input("Enter '1' to encrypt passwords.txt, '2' to decrypt passwords.txt.enc: ")

    if choice == '1':
        encrypt_file('passwords.txt', key)
        with open('passwords.txt.enc.salt', 'wb') as salt_file:
            salt_file.write(salt)
        print("File encrypted successfully.")
    elif choice == '2':
        try:
            with open('passwords.txt.enc.salt', 'rb') as salt_file:
                salt = salt_file.read()
            key = generate_key(password, salt)
            decrypted_data = decrypt_file('passwords.txt.enc', key)
            with open('passwords.txt', 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
            print("File decrypted successfully.")
        except FileNotFoundError:
            print("Encrypted file not found. Please encrypt the file first.")
        except Exception as e:
            print(f"Error decrypting file: {e}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()