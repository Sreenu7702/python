# n=153
# s=0
# d=n
# while(d>0):
#     r=d%10
#     s=s+r**3
#     d=d//10
# if(s==n):
#     print("armstrong")
# else:
#     print("not armstrong")

n=int(input("enter the num"))
s=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+r**b
    n=n//10
if sum1==s:
    print("armstrong")
else:
    print("not armstrong")