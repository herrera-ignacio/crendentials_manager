class Cipher:
    def __init__(self, algorithm, secret):
        self.secret = secret
        self.algorithm = algorithm

    def encrypt(self, text):
        return self.algorithm.encrypt(text, self.secret)

    def decrypt(self, text):
        return self.algorithm.decrypt(self, self.secret)