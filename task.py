num=float('-inf')
print(num)
num=float('inf')
print(num)

num=float('inf')
list=[100,1000,10000,1000000]
for i in list:
    if i<num:
        num=i
print(num)

num=float('-inf')
list=[100,1000,10000,1000000]
for i in list:
    if i<num:
        num=i
print(num)
#float methods
#used to convert integre to float
num=100
print(float(num))

num=float('-inf')
list=[-20,30,-50,10]
for i in range(len(list)):
    if abs(list[i])>num:
        num=abs(list[i])
print(num)
#divmod method
#used to return the quotient and remainder of a division
#answer is in tuple format
num=245
print(divmod(num,10))
#complex method
#used to convert a string or a number into a complex number 
num=3+5j
print(complex(num))
num=4
img_val=10
print(complex(num,img_val))
#abs method
#used to return the absolute value of a number
num=-20
print(abs(num))
#type method
#used to return the type of a variable
num=10.00
print(type(num))
num=10
print(isinstance(num,int))
#using function to find boolean value of a number in isinstance method
num=[10,10.0,11,11.0,12,13]
def is_inst(i):
    return isinstance(i,int)
res=[is_inst(i) for i in num]
print(res)
#math module
import math
num=5
print(math.factorial(num))
#ceil method
num=5.1
print(math.ceil(num))
#trunc method
num=5.9
print(math.trunc(num))
#floor method
num=5.9
print(math.floor(num))
#gcd method
num1=20
num2=30
print(math.gcd(num1,num2))
#lcm method
num1=20
num2=30
print(math.lcm(num1,num2))
#sqrt method
num=25
print(math.sqrt(num))
#pow method
num=5
print(math.pow(num,3))