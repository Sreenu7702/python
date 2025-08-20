#for x in range(1,10):
#   print(x)
#for i in range(1,10):
#    print("Hello Sreenu")
#for x in range(1, 10):
#    print(f"2x{x}={x*2}")

#for i in range(10, 1,-1):
#   print(i)
#check voting eligibility
#l1=["sravan","harish","aravind","akhil"]
#l2=[24,17,20,18]
#for i in range(len(l1)):
#    if l2[i] >= 18:
#        print(l1[i]," -",l2[i],"-", "is eligible to vote")
#   else:
#        print(l1[i]," -",l2[i],"-", "is not eligible to vote")

#n=int(input("Enter a number: "))
#sum=0
#while n > 0:
#   digit = n % 10
#    sum += digit
#   n //= 10
#print("Sum of digits:", sum)

amount = 21
chocolates = amount
wrappers = chocolates

while wrappers >= 3:
    extra = wrappers // 3
    chocolates += extra
    wrappers = wrappers % 3 + extra

print("Total chocolates you can eat:", chocolates)