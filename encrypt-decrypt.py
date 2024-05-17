import os
from hashlib import sha256

#directory PATH from where you execute the program
directory = '../toencrypt/'

#key for the encryption/decryption
key = 'test'

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

def decrypt(toencrypt: str, output: str, key:str):
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

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        ext = f[f.find(".", 4) + 1:]
        if ext == "crypt":
            decrypt(f, f[:f.find(".", 4) + 1] + "txt", key)
        else:
            encrypt(f, f[:f.find(".", 4) + 1] + "crypt", key)
        os.remove(f)