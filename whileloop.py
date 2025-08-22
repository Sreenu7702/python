#it id know where to start
#it is know where to end
#it is know how to update
#while(condition):
# statements
for x in range(10):
    print(x)
#while True:
    print("Hello")
x=1
while(x<=10):
    print(x)
    x+=1
str1="Hello"
i=len(str1)-1
while i >=0:
    print(str1[i], end=' ')
    i -= 1
list1=['krishna', 'ram', 'sita', 'radha']
i=0
# while i < len(list1):
#     print(list1[i], end=' ')
#     i += 1
i=len(list1) - 1
while i >= 0:
    print(list1[i], end=' ')
    i -= 1

#rev number
num =12540
while(num>0):
    ld=num%10
    print(ld)
    num=num//10

num=852147
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)

ip=12521
ip1=ip
rev=0
while(ip>0):
    ld=ip%10
    rev=rev*10+ld
    ip=ip//10
print(rev)
if(ip1==rev):
    print("is palindrome")
else:
    print("not a palindrome")

num=125
sum=0
while(num>0):
    ld=num%10
    sum+=ld 
    num=num//10
print(sum)

#find the length of given num without converting into string
num = 123456
length = 0
while num > 0:
    num //= 10
    length += 1
print( length)

#write Amstrong number or not
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

# sum of only even numbers in given ip
# count only odd numbers in given ip
num = 123456789
sum_even = 0
count_odd = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum_even += digit
    else:
        count_odd += 1
    num //= 10
print( sum_even)
print( count_odd)
