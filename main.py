
from decorators import log_execution

@log_execution
def my_function():
    print("Виконується основна функція.")

if __name__ == "__main__":
    my_function()