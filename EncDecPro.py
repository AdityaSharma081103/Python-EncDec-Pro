import cryptography
import rsa
from cryptography.fernet import Fernet

def display_menu():
    print("\n Python EncDec Pro ")
    print("----------------------------------------- ")
    print(" 1. Encrypt Symmetric")
    print(" 2. Decrypt Symmetric")
    print(" 3. Generate RSA Keys ")
    print(" 4. Encrypt Asymmetric ")
    print(" 5. Decrypt Asymmetric ")
    print(" 0. EXIT")
    print("" \
    "---------------------------------------")

 #---------------------------------------#

from cryptography.fernet import Fernet
def Encrypt_Symmetric():
# Generate a key (only once, then reuse)
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Encrypt
    text = input("Enter text to encrypt (symmetric): ").encode()
    encrypted = fernet.encrypt(text)

    print("Key:", key.decode())  # Save this key to decrypt later
    print("Encrypted:", encrypted.decode())

 #---------------------------------------#


#---------------------------------------#

from cryptography.fernet import Fernet
def Decrypt_Symmetric():
    # Enter the key and encrypted text from step 1
    key = input("Enter the symmetric key: ").encode()
    encrypted = input("Enter the encrypted text: ").encode()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)

    print("Decrypted:", decrypted.decode())

#---------------------------------------#


#---------------------------------------#

import rsa
def Generate_RSA_Keys():
    # Generate keys
    public_key, private_key = rsa.newkeys(512)

    # Save keys to files
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1())

    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1())

    print("RSA Keys generated and saved as public.pem & private.pem")

#---------------------------------------#


#---------------------------------------#

import rsa
def Encrypt_Asymmetric():
    # Load public key
    with open("public.pem", "rb") as pub_file:
        public_key = rsa.PublicKey.load_pkcs1(pub_file.read())

    # Encrypt message
    message = input("Enter text to encrypt: ").encode()
    encrypted = rsa.encrypt(message, public_key)

    print("Encrypted message:", encrypted)

#---------------------------------------#


#---------------------------------------#

import rsa
def Decrypt_Asymmetric():
    # Load private key
    with open("private.pem", "rb") as priv_file:
        private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())

    # Paste the encrypted message (from encryption step)
    encrypted = eval(input("Enter encrypted bytes: "))

    # Decrypt
    decrypted = rsa.decrypt(encrypted, private_key).decode()

    print("Decrypted message:", decrypted)

#---------------------------------------#


def main():
    while True:
        display_menu()
        choice = input("Enter Your choice (0-5) : ")
        

        if choice == "1" : 
            print("You have Selected : Encrypt Symmetric")
            Encrypt_Symmetric()

        elif choice == "2":
            print("You have Selected : Decrypt Symmetric")
            Decrypt_Symmetric()

        elif choice == "3":
            print("You have Selected : Generate RSA Keys ")
            Generate_RSA_Keys()

        elif choice == "4":
            print("You have Selected : Encrypt Asymmetric ")
            Encrypt_Asymmetric()

        elif choice == "5":
            print("You have Selected : Decrypt Asymmetric ")
            Decrypt_Asymmetric()

        elif choice == "0":
            print("You have been Exit")
            break

        else :
            print("Enter other number ")

if __name__=="__main__":
    main()
