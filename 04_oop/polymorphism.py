# Demonstrating polymorphism in Python

class Bird:
    def speak(self):
        return "Chirp!"

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Function that uses polymorphism
def animal_sound(animal):
    print(animal.speak())

# --- Test calls ---
animals = [Bird(), Dog(), Cat()]

for a in animals:
    animal_sound(a)
