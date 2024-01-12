from cryptography.fernet import Fernet
import os

def get_password_file_path():
    return os.path.join(os.getcwd(), 'passwords.txt')

def generate_key():
    return Fernet.generate_key()

def load_or_generate_key():
    key_file = 'secret.key'
    if os.path.exists(key_file):
        with open(key_file, 'rb') as file:
            key = file.read()
    else:
        key = generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
    return key

def encrypt_password(password, key):
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password

def save_password(username, password, url):
    key = load_or_generate_key()
    encrypted_password = encrypt_password(password, key)
    
    with open(get_password_file_path(), 'a') as file:
        file.write(f"{username}:{encrypted_password}:{url}\n")

def decrypt_and_print_password(username):
    key = load_or_generate_key()

    with open(get_password_file_path(), 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 3 and parts[0] == username:
                encrypted_password = parts[1]
                url = parts[2]
                encrypted_password = encrypted_password.lstrip("b'")
                encrypted_password = encrypted_password.rstrip("'")
                
                try:
                    decrypted_password = decrypt_password(encrypted_password.encode(), key)
                    print(f"Username: {username}, Password: {decrypted_password}, Descrizione (URL or OS login): {url}")
                    return
                except Exception as e:
                    print(f"Error decrypting password for {username}: {e}")
                    return

    print(f"Password for {username} not found.")

def main():
    choice = input("Enter '1' to save a password, '2' to decrypt and print a password: ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        url = input("Enter Description (URL or OS login): ")
        save_password(username, password, url)
        print("Password saved successfully.")
    elif choice == '2':
        username_to_decrypt = input("Enter username to decrypt password: ")
        decrypt_and_print_password(username_to_decrypt)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()