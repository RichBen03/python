# creating a function that checks for time it wraps a function (decorator)

import time #importing the time library

def timer_decorator(func): # creating a fuunction that takes another function as input.The function that will run is finc
    def wrapper(*args, **kwargs): #  defining another function called wrapper that will run instead of the original function (func). The *args and **kwargs allow wrapper to accept any number of arguments and keyword arguments, just like the original function.
        start_time = time.time()  # getting the current time in seconds and store it in start_time. This is the moment just before func is called.
        result = func(*args, **kwargs)  # Execute the function and store its result
        end_time = time.time()  # Record the end time after the function completes
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute.")
        return result  # Return the result of the function
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)  # Simulate a slow operation with a 2-second delay
    return "Finished slow function"

@timer_decorator
def quick_function():
    sum([i for i in range(100)])  # Perform a quick operation
    return "Finished quick function"
@timer_decorator
def compute_sum(n):
    total = sum(range(n))  # Sum all numbers up to n
    return total

print(slow_function())
print(quick_function())
print(compute_sum(1000000))