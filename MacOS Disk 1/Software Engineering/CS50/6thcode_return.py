def main():
    x = int(input("Enter a number: "))
    print("X squared is", square(x))

def square(n):
    return n * n # n ** 2 // pow(n, 2) all are valid

main()
