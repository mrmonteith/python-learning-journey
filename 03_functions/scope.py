# Demonstrating local vs global scope
x = 10

def change_x():
    global x
    x = 20

print("Before:", x)
change_x()
print("After:", x)
