def create_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return matrix

my_matrix = create_matrix()
print("Basic 3x3 Matrix:")
for row in my_matrix:
    row.reverse()
    print(row)


m=[]
n=3
for _ in range(n):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(n):
    for j in range(n-1,-1,-1):
        print(m[j][i],end=" ")
    print()

# X-hallow pattern
n=5
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#squre pattren
n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==5-1 or j==0 or j==5-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# n=5
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "*n)
#     else:
#         print("* "+" "*(n-2)+"* ")
#use single loop
# n=5
# for i in range(n*n):
#     if(i<n or i>=n*(n-1) or i%n==0 or i%n==n-1):
#         print("*",end=" ")
#     else:
#         print(" ",end=" ")
#     if(i%n==n-1):
#         print()

#right angle triangle
n=5
for i in range(n):
    for j in range(i+1):
        if( j==0 or i==n-1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#single loop
n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*i)
    else:
        print("* "+" "*(i-2)+"* ")
n=5
for i in range(n):
    for j in range(n-i):
        if(i==0 or j==0 or j==n-i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

#resv right angle triangle
n=5
for i in range(1,n+1):
    s="  "*(n-i)
    if i==1 or i==n:
        print(s+"* "*i)
    else:
        print(s+"* "+"  "*(i-2)+"*")

#diamond hallow pattern
n=5
for i in range(1,n+1):
    s=" "*(n-i)
    if i==1:
        print(s+"*")
    else:
        print(s+"* "+"  "*(i-2)+"*")
for i in range(n-1,0,-1):
    s=" "*(n-i)
    if i==1:
        print(s+"*")
    else:
        print(s+"* "+"  "*(i-2)+"*")