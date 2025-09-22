n=5
for i in range(n,0,-1):
    s=" "*(n-i)
    if i==1:
        print(s+"* "*(i))
    else:
        print(s+"* "+"  "*(i-2)+"*")
for i in range(2,n+1):
    s=" "*(n-i)
    if i==1:
        print(s+"* "*(i))
    else:
        print(s+"* "+"  "*(i-2)+"*")

# size of the butterfly
n = 5
# Upper half
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(1, 2*(n-i)+1):
        print(" ", end="")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(1, 2*(n-i)+1):
        print(" ", end="")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()



#recursion
# import sys
# print(sys.getrecursionlimit())
# i=0
# def greeting():
#     global i
#     i+=1
#     print("Hello",i)
#     greeting()
# greeting()

n=10
sum=0
for i in range(1,11):
    sum+=i
print(sum)

#sum of n numbers without using loop
#factorial
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#palidrome 
s="madam"
f=0
i=0
j=len(s)-1
while i<j:
    if s[i] == s[j]:
        i+=1
        j-=1
    else:
        f=1
        break
if f==1:
    print("not palindrome")
else:
    print("palindrome")

#palindrome using recursion

def palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
print(palindrome("madam"))

# def pal(s,i,j):
#     if i>j:
#         return "palindrome"
#     if s[i] !=s[j]:
#         return "not palindrome"
#     return pal(s,i+1,j-1)
# s="madam"
# i=0
# j=len(s)-1
# print(pal(s,i,j))

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i), end=" ")
