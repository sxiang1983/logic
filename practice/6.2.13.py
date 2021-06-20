for i in range(2,11):
    for j in range(i, 11):
        print(" ", end=" ")
    for j in range(1, i):
        print(j, end=" ")
    for j in range(i-2, 0, -1):
        print(j, end=" ")
    print()

for i in range(9,1,-1):
    for j in range(i, 11):
        print(" ", end=" ")
    for j in range(1, i):
        print(j, end=" ")
    #for j in range(i-2, 0, -1):
    #    print(j, end=" ")
    print()
