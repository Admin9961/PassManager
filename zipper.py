import zipfile
import os

def zip_files():
    zip_name = 'encrypted_files.zip'
    
    files_to_zip = ['passwords.txt.enc', 'secret.key', 'passwords.txt.enc.salt']

    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for file in files_to_zip:
            if os.path.exists(file):
                zip_file.write(file, os.path.basename(file))
                print(f"{file} added to {zip_name}")
            else:
                print(f"{file} not found. Skipped.")

    print("Compressione completata con successo. Eliminazione dei file originali...")
    
    for file in files_to_zip:
        try:
            os.remove(file)
            os.remove("passwords.txt")
            print(f"{file} eliminato.")
        except Exception as e:
            print(f"Errore durante l'eliminazione di {file}: {e}")

def main():
    response = input("Vuoi salvare in una .ZIP passwords.txt.enc, passwords.txt.enc.salt e secret.key? (sì/no): ").lower()

    if response == 'si' or response == 'sì':
        zip_files()
        print("File ZIP creato con successo.")
    elif response == 'no':
        print("Ok, ciaone!")
    else:
        print("Risposta non valida. Terminazione.")

if __name__ == "__main__":
    main()
