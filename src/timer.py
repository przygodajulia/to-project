import time
import functools

class ExecutionTimeDecorator:
    """
    A decorator class to measure the execution time of a function.

    Attributes:
        func (function): The function to be decorated.

    """
    
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print(f"Execution started...\n")
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {self.func.__name__}: {execution_time:.4f} seconds")
        return result