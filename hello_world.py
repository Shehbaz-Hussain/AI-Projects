# hell0_world.py - My very first python file
# Shehbaz AI Systems - AI Engineering Journey

print("Hello AI World")
print("My AI Journey begins today.")
print("Shehbaz AI Systems - Building one step at a Time.")

# Basic operations

print(2 + 8)
print(6 - 3)
print(3 * 34)
print(89 / 5)

name = "Shehbaz"
age = 20
semester = 2

print("Name:", name)
print("Age:", age)
print("Semester:", semester)

name = "AI Student"
age = 20
cgpa = 3.5
is_student = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

birth_year = input("Enter your birth year: ")

current_year = 2026

age = current_year - int(birth_year)

print("Your age is:", age)


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = int(num1) + int(num2)

print("Sum =", result)


length = 10
width = 5

area = length * width

print("Area =", area)


math = 80
python = 90
ai = 85

total = math + python + ai

average = total / 3

print("Total Marks:", total)
print("Average:", average)


number = int(input("Enter number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")


marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

else:
    print("Fail")