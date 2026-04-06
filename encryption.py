#citation: https://www.youtube.com/watch?v=FjTn7KlOZtQ&t=37s

from cryptography.fernet import Fernet
import os

def load_key():
    with open('encryptionkey.key', 'rb') as file:
        return file.read()
#opens the first key generated w/o risk of complicating things if/when another key is generated
#this problem was discussed in the tutorial

def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

#DECRPYTED
# key = 'QY93MrgI3IgZUd-n-K7efLp1b64inPi4b79PhDFw44M='
# fernet = Fernet(key)
#c
# with open('shapes_encrypted.csv', 'rb') as enc_file:
#     for line in enc_file:
#         decrypted = fernet.decrypt(line.strip())
#         print(decrypted.decode())

