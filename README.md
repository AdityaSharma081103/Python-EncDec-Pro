# Python-EncDec-Pro

**Python EncDec Pro** is a simple encryption/decryption tool built in Python.  
It supports both **symmetric (Fernet/AES)** and **asymmetric (RSA)** encryption.  

---

## Features

1. **Encrypt Symmetric**  
   - Encrypt text using a single secret key.  
   - Key must be saved to decrypt later.  

2. **Decrypt Symmetric**  
   - Decrypt text using the symmetric key.  

3. **Generate RSA Keys**  
   - Generate a public/private key pair for asymmetric encryption.  
   - Keys are saved as `public.pem` and `private.pem`.  

4. **Encrypt Asymmetric**  
   - Encrypt text using the RSA public key.  

5. **Decrypt Asymmetric**  
   - Decrypt text using the RSA private key.  

---

## How to Use

1. Clone this repository:

2.	Install dependencies:  
pip install cryptography rsa

3.	Run the tool:  
python EncDec-Pro.py    
   
