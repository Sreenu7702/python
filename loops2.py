#check vote eligibility
l1 = ["sravan", "harish", "aravind", "akhil"]
l2 = [24, 17, 20, 18]
for i in range(len(l1)):
    if l2[i] >= 18:
        print(l1[i], "-", l2[i], "-", "is eligible to vote")
    else:
        print(l1[i], "-", l2[i], "-", "is not eligible to vote")

#Sum of digits
n=123
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
print("Sum of digits:", sum_of_digits)

#Highest digit in an integer
n=123498
highest_digit = 0
while n > 0:
    digit = n % 10
    if digit > highest_digit:
        highest_digit = digit
    n //= 10
print("Highest digit:", highest_digit)

# Chocolates from wrappers
amount = 21
chocolates = amount
wrappers = chocolates
while wrappers >= 3:
    extra = wrappers // 3
    chocolates += extra
    wrappers = wrappers % 3 + extra
print("Total chocolates you can eat:", chocolates)
