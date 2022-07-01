from cryptography.fernet import Fernet

import os

# Cryptographic protection

def file_exists(filename, filekey):
    return os.path.isfile(filename), os.path.isfile(filekey)

def load_key(filekey):
    return open(filekey, 'rb').read()

def decrypt(filename, key):
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    return Fernet(key).decrypt(encrypted_data)

def crypto_data(filename, filekey):
    name, key = file_exists(filename, filekey)
    if not name:
        return 'Ошибка!', 'Не найден криптофайл!'
    if not key:
        return 'Ошибка!', 'Не найден криптоключ!'
    data = str(decrypt(filename, load_key(filekey)))[:-1]
    return data[2:12], data[16:]

