import os
from hashlib import sha256

#change line 8 and line 11 with your values and then run the program to encrypt or decrypt all files in a directory

#directory PATH of the dir containing files to encrypt/decrypt
directory = 'PATH/TO/THE/DIR/YOU/WANT/TO/ENCRYPT/OR/DECRYPT'

#key for the encryption/decryption files
key = 'YOUR KEY'

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

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        base_path = f[:f.rfind('/')] + '/'
        ext = f[f.rfind(".") + 1:]
        print(base_path)
        print(ext)
        if ext == "crypt":
            decrypt(f, f[:f.rfind(".")], key)
        else:
            encrypt(f, f + ".crypt", key)
        os.remove(f)