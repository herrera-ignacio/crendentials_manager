from Crypto.Cipher import AES
from business.entities.CipherAlgorithm import CipherAlgorithm

class AESAlgorithm(CipherAlgorithm):
    def __init__(self, key, iv):
        self.name = 'AES'
        self.key = key
        self.iv = iv

    def encrypt(self, text):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(text)

    def decrypt(self, encrypted_text):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.decrypt(encrypted_text)

def test():
    message = 'Nacho cipher msg'

    cipher = AESAlgorithm('This is a key123', 'This is an iv456')
    message = cipher.encrypt(message)
    print(message)
    message = cipher.decrypt(message)
    print(message)
