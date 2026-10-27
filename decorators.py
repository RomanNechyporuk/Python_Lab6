
def log_execution(func):
    def wrapper(*args, **kwargs):
        print("Увага, функція працює!")
        return func(*args, **kwargs)
    return wrapper