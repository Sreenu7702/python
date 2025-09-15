#pyramid pattern
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

#diamond pattern
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

#left alined half daimond
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end=" ")
    print()

# Right-Aligned Half Diamond
n = 5

# upper part
for i in range(1, n+1):
    print("  "*(n-i) + "* " * i)

# lower part
for i in range(n-1, 0, -1):
    print("  "*(n-i) + "* " * i)
