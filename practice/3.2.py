a=3
if a == 1:
    print("If a is one, this will print.")
    print("So will this.")
    print("And this.")
 
print("This will always print because it is not indented.")

b=2
c=3

# And
if a < b and a < c:
    print("a is less than b and c")
 
# Non-exclusive or
if a < b or a < c:
    print("a is less than either b or c (or both)")

# Boolean data type. This is legal!
a = True
if a:
    print("a is true")

a = True
b = True
 
if a and b:
    print("a and b are both true")

temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not hot outside")
print("Done")
