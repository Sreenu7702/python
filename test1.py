#print hallow diamond
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

#print nearest prime number
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=7
if prime(n):
    print(n)
else:
    left=n-1
    right=n+1
    while True:
        if prime(left):
            print(left)
            break
        if prime(right):
            print(right)
            break
        left -=1
        right +=1

#find repeated values in a list
a=[1,2,3,4,5,1,2,3,6,7,8,9,10]
b=[]
for i in a:
    if a.count(i)>1 and i not in b:
        b.append(i)
print(b)

#replace built in functions of string
def replace(original, old, new):
    result = ""
    i = 0
    while i < len(original):
        if original[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += original[i]
            i += 1
    return result

text = "Sravan"
old = "a"
new = "b"
print(replace(text, old, new))

#product of two matrices
A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
B = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]
C = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
print(C)
