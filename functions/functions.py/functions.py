# functions_guide.py

# 1. Basic Function
# This is a simple function that prints a greeting.
def greet():
    print("Hello, world!")

# Call the function
greet()


# 2. Function with Parameters
# This function takes a name as a parameter and greets the person.
def greet(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")


# 3. Return Statements
# This function takes two numbers, adds them, and returns the result.
def add(a, b):
    return a + b

# Call the function and store the result
result = add(5, 3)
print("Result:", result)


# 4. Default Parameters
# This function greets the person with a default name if no name is provided.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Uses the provided argument
greet()  # Uses the default value "Guest"


# 5. Keyword Arguments
# This function demonstrates using keyword arguments to pass parameters.
def describe_pet(animal_type="dog", pet_name="Rex"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="cat", pet_name="Whiskers")  # Order doesn’t matter
describe_pet(pet_name="Spot")  # Only pet_name is provided; animal_type uses default


# 6. Variable-Length Arguments (*args)
# This function accepts a variable number of arguments and adds them.
def add_multiple(*args):
    return sum(args)

print("Sum:", add_multiple(1, 2, 3, 4, 5))  # Adds multiple numbers


# 7. Variable-Length Keyword Arguments (**kwargs)
# This function accepts a variable number of keyword arguments.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Wonderland")


# 8. Lambda Functions
# A lambda function is a small anonymous function.
multiply = lambda x, y: x * y
print("Lambda multiply:", multiply(3, 4))


# 9. Nested Functions
# A function within another function.
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the nested function!")


# 10. Closures
# A closure is a function object that remembers values in enclosing scopes.
def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

times_two = make_multiplier(2)
print("Closure multiply:", times_two(5))  # Output is 10


# 11. Recursion
# A recursive function is a function that calls itself.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# 12. Decorators (Advanced)
# Decorators are functions that modify the behavior of another function.
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()


# 13. Generator Functions
# A generator is a function that yields items instead of returning them.
def countdown(num):
    while num > 0:
        yield num
        num -= 1

for count in countdown(5):
    print("Countdown:", count)


# 14. Function Annotations
# Function annotations provide hints about the types of arguments and return values.
def add_with_annotations(a: int, b: int) -> int:
    return a + b

print("Add with annotations:", add_with_annotations(3, 4))
