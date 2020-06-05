from utils import open_file

class Writer:
    def __init__(self, filename):
        self.filename = filename

    @open_file('r+')
    def set_columns(self, f, column_names):
        data = f.readlines()
        row = f'{",".join(name for name in column_names)}\n'
        if (len(data) > 0):
            data[0] = row
            f.seek(0, 0)
            f.truncate()
            f.writelines(data)
        else:
            f.write(row)

    @open_file('a')
    def add_record(self, f, id, values):
        f.write(f'{id},{",".join([str(value) for value in values])}\n')
