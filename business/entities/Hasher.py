class Hasher:
    def __init__(self, hash, reverse_hash, secret):
        self.hash = hash
        self.reverse_hash = reverse_hash
        self.secret = secret

    def hash(self, text):
        return self.hash(text, self.secret)

    def reverse_hash(self, text):
        return self.reverse_hash(self, self.secret)