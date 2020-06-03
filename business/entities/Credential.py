class Credential:
    def __init__(self, id, source, user, password):
        self.id = id
        self.source = source
        self.user = user
        self.password = password

    def encrypt(self, hash):
        self.source = hash(self.source)
        self.user = hash(self.user)
        self.password = hash(self.password)

    def decrypt(self, reverse_hash):
        self.source = reverse_hash(self.source)
        self.user = reverse_hash(self.user)
        self.password = reverse_hash(self.password)
        