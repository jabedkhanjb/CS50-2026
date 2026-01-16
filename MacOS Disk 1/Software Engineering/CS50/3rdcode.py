"""
x = int(input("Enter a number: "))
y = 2

z = x + y
print(z)

print(int(input("Enter the 1st number: ")) + int(input("Enter the 2nd number: ")))

j = float(input("Enter a float number: "))
b = float(input("Enter another float number: "))

m = round(j + b, 1)
print(f"{m:,}")
"""

x = float(input("Enter a float number: "))
y = float(input("Enter another float number: "))    

z = round(x / y, 2)
print(f"{z:.2f}")