
my_list = [ [2,3], [4,3], [6,7] ]
for item in my_list:
    print(item)



my_list = [101, 20, 10, 50, 60]
for i in range(len(my_list)):
    print(my_list[i])
# Copy of the array to sum
my_list = [5,76,8,5,3,3,56,5,23]
 
# Initial sum should be zero
list_total = 0
 
# Loop from 0 up to the number of elements
# in the array:
for i in range(len(my_list)):
    # Add element 0, next 1, then 2, etc.
    list_total += my_list[i]
 
# Print the result
print("list_total: ", list_total)


x = "This is a sample string"
#x = "0123456789"
 
print("x=", x)
 
# Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])
 
# Accessing from the right side
print("x[-1]=", x[-1])
 
# Access 0-5
print("x[:6]=", x[:6])
# Access 6
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])





a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))





plain_text = "This is a test. ABC abc"
 
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end="")


print()


# Create an empty associative array
# (Note the curly braces.)
x = {}
 
# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1
 
# Fetch and print an item
print(x["fred"])
