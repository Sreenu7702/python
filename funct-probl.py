#Area of Square
def area_of_square(side_length):
    return side_length * side_length
print(area_of_square(4))  # Output: 16
print(area_of_square(5))  # Output: 25

#Area of Rectangle
def area_of_rectangle(length, width):
    return length * width
print(area_of_rectangle(4, 5))
print(area_of_rectangle(6, 3))  # Output: 18

#Area of Triangle
def area_of_triangle(base, height):
    return 0.5 * base * height
print(area_of_triangle(4, 5))
print(area_of_triangle(6, 3))  # Output: 9.0

#perimeter of Rectangle
def perimeter_of_rectangle(length,breadth):
    return 2 * (length + breadth)
print(perimeter_of_rectangle(4, 5))  # Output: 18
print(perimeter_of_rectangle(5,3))  # Output: 16

#perimeter of Square
def perimeter_of_square(side_length):
    return 4 * side_length
print(perimeter_of_square(4))  # Output: 16
print(perimeter_of_square(5))  # Output: 20

#perimeter of Triangle
def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3
print(perimeter_of_triangle(3, 4, 5))  # Output: 12
print(perimeter_of_triangle(5, 12, 13))  # Output: 30

#break amount into 1000s,500s,and remaining charge
def break_amount(amount):
    thousands = amount // 1000
    amount %= 1000
    five_hundreds = amount // 500
    amount %= 500
    return thousands, five_hundreds, amount
print(break_amount(3700))

#sun of marks(maths,physics,chemistry)
def sum_of_marks(maths, physics, chemistry):
    return maths + physics + chemistry
print(sum_of_marks(85, 90, 78))  # Output: 253
#average of marks(maths,physics,chemistry)
def average_of_marks(maths, physics, chemistry):
    total = sum_of_marks(maths, physics, chemistry)
    return total / 3
print(average_of_marks(85, 90, 78))  # Output: 84.33

#convert seconds to hours, minutes, and seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds
print(convert_seconds(3672))  # Output: (1, 1, 12)

#check even or odd
x=int(input("Enter the number"))
if x%2==0:
    print("even number")
else:
    print("odd number")

#divisible by 2,3 and 6
x=int(input("Enter the number :"))
if x%2==0 and x%3==0 and x%6==0:
    print("divisible by 2,3 and 6")
else:
    print("not divisible by 2,3 and 6")