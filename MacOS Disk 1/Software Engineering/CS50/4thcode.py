def hello():
    print("Hello")

name = input("Enter your name: ")
hello()
print(name)

def hello(to):
    print("Hello,", to)

name = input("Enter your name: ")
hello(name)

def hello(to="World!"):
    print("Hello,", to)
hello()
name = input("Enter your name: ")
hello(name)