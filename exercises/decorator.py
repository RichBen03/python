# creating a function that checks for time it wraps a function
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time before calling the function
        result = func(*args, **kwargs)  # Execute the function and store its result
        end_time = time.time()  # Record the end time after the function completes
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute.")
        return result  # Return the result of the function
    return wrapper