#print 100 to 0 in reverse which is divisible by 5
for i in range(100, -1, -5):
    print(i)

#check given string is palindrome or not using function
def is_palindrome(s):
    return s == s[::-1]
s = "madam"
if is_palindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

#print tables in reverse order using function
def print_table(n):
    for i in range(10, 0, -1):
        print(f"{n} x {i} = {n * i}")
n = 5
print_table(n)
