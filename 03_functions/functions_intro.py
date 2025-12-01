# Basic function definition
def greet(name):
    return f"Hello, {name}!"

# Function with default argument
def greet_default(name="World"):
    return f"Hello, {name}!"

# Function with multiple arguments
def add_numbers(a, b):
    return a + b

# Function with keyword arguments
def describe_pet(pet_name, animal_type="dog"):
    return f"I have a {animal_type} named {pet_name}."

# Function with recursion (factorial)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# --- Test calls ---
print(greet("Michael"))
print(greet_default())
print(add_numbers(5, 7))
print(describe_pet("Buddy"))
print(describe_pet("Whiskers", "cat"))
print(f"Factorial of 5 is {factorial(5)}")
