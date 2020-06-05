def open_file(mode):
    def handle_file(func):
        def wrapper(instance, *args):
            with open(instance.filename, mode) as f:
                print(*args)
                func(instance, f, *args)
        return wrapper
    return handle_file
