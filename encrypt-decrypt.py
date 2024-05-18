import os
from hashlib import sha256
from cryptography.fernet import Fernet

#directory PATH of the dir containing files to encrypt/decrypt
directory = '../toencrypt/'

#key for the encryption/decryption files
key = 'test'

fkey = Fernet.generate_key()
fernet = Fernet(fkey)

def encrypt(toencrypt: str, output: str, key:str):
    keys = sha256(key.encode('utf-8')).digest()
    with open(toencrypt, 'rb') as f_toencrypt:
        with open(output, 'wb') as f_output:
            i = 0
            while f_toencrypt.peek():
                c = ord(f_toencrypt.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_output.write(b)
                i += 1

def decrypt(todecrypt: str, output: str, key:str):
    keys = sha256(key.encode('utf-8')).digest()
    with open(todecrypt, 'rb') as f_todecrypt:
        with open(output, 'wb') as f_output:
            i = 0
            while f_todecrypt.peek():
                c = ord(f_todecrypt.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_output.write(b)
                i += 1

def crypt_filename(filename: str) -> str:
    encfilename = fernet.encrypt(filename.encode())
    return(encfilename)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        ext = f[f.find(".", 4) + 1:]
        base_path = f[:f.rfind('/')] + '/'
        print(base_path)
        if ext == "crypt":
            decrypt(f, fernet.decrypt(fname).decode(), key)
        else:
            encrypt(f, base_path + str(fernet.encrypt(filename.encode())) + ".crypt", key)
        os.remove(f)