from utils import open_file

class Reader:
    def __init__(self, filename):
        self.filename = filename
    
    @open_file('r')
    def get_rows(self, f):
        data = f.readlines()
        return data
    
    @open_file('r')
    def get_row(self, f, id):
        try:
            data = f.readlines()
            return data[id]
        except IndexError:
            print('Invalid row')
