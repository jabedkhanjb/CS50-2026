def main():
    name = input("Enter your name: ").strip().title()
    hello(name)
    
    
def hello(to="World!"):
    print("Hello,", to)
hello() 
main()




