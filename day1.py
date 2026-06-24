"""
DAY 1 - PYTHON BASICS COMPLETE SOLUTION

Topics:
- Variables
- Data Types
- Input / Output
- Type Conversion
- Operators
- Conditions
- CLI Programs

"""


# ==========================================
# SECTION 1: VARIABLES AND DATA TYPES
# ==========================================

print("===== VARIABLES AND DATA TYPES =====")


name = "Shehbaz"

age = 20

cgpa = 3.5

is_ai_student = True


print("Name:", name)

print("Age:", age)

print("CGPA:", cgpa)

print("AI Student:", is_ai_student)



print(type(name))

print(type(age))

print(type(cgpa))

print(type(is_ai_student))



# ==========================================
# SECTION 2: BASIC OPERATIONS
# ==========================================


print("\n===== BASIC OPERATIONS =====")


a = 20

b = 5


print("Addition:", a + b)

print("Subtraction:", a - b)

print("Multiplication:", a * b)

print("Division:", a / b)

print("Modulus:", a % b)

print("Power:", a ** 2)



# ==========================================
# SECTION 3: USER INFORMATION SYSTEM
# ==========================================


print("\n===== USER INFORMATION =====")


user_name = input("Enter your name: ")

user_city = input("Enter your city: ")


print(
    f"My name is {user_name} and I live in {user_city}"
)



# ==========================================
# SECTION 4: TYPE CONVERSION PRACTICE
# ==========================================


print("\n===== TYPE CONVERSION =====")


number1 = input("Enter first number: ")

number2 = input("Enter second number: ")



print("Before conversion:")

print(type(number1))



number1 = int(number1)

number2 = int(number2)



print("After conversion:")

print(type(number1))



sum_result = number1 + number2


print("Sum:", sum_result)



# ==========================================
# SECTION 5: MARKS AND PERCENTAGE CALCULATOR
# ==========================================


print("\n===== MARKS CALCULATOR =====")


python_marks = float(input("Python marks: "))

math_marks = float(input("Math marks: "))

database_marks = float(input("Database marks: "))



total_marks = (
    python_marks
    + math_marks
    + database_marks
)


percentage = (
    total_marks / 300
) * 100



print(f"Total Marks: {total_marks}")

print(f"Percentage: {percentage}%")



# ==========================================
# SECTION 6: CLI CALCULATOR
# ==========================================


print("\n===== CLI CALCULATOR =====")



first_number = float(
    input("Enter first number: ")
)


operator = input(
    "Enter operation (+,-,*,/,%): "
)


second_number = float(
    input("Enter second number: ")
)



if operator == "+":

    result = first_number + second_number



elif operator == "-":

    result = first_number - second_number



elif operator == "*":

    result = first_number * second_number



elif operator == "/":

    if second_number == 0:

        result = "Error: Division by zero"

    else:

        result = first_number / second_number



elif operator == "%":

    result = first_number % second_number



else:

    result = "Invalid operator"



print(f"Result: {result}")



# ==========================================
# SECTION 7: AGE CALCULATOR
# ==========================================


print("\n===== AGE CALCULATOR =====")



person_name = input("Enter your name: ")


person_age = int(
    input("Enter your age: ")
)



future_age = person_age + 1



print(
    f"Hello {person_name}, next year you will be {future_age} years old"
)



# ==========================================
# SECTION 8: AI STUDENT PROFILE SYSTEM
# ==========================================


print("\n===== AI PROFILE SYSTEM =====")



student_name = input("Student name: ")

student_age = int(
    input("Student age: ")
)

skill = input(
    "Current skill: "
)

goal = input(
    "Career goal: "
)



print("\n----- PROFILE -----")


print(
    f"Name: {student_name}"
)


print(
    f"Age: {student_age}"
)


print(
    f"Skill: {skill}"
)


print(
    f"Goal: {goal}"
)



# ==========================================
# SECTION 9: SIMPLE LOGIN SYSTEM
# ==========================================


print("\n===== LOGIN SYSTEM =====")



correct_password = "python123"


password = input(
    "Enter password: "
)



if password == correct_password:

    print("Login successful")


else:

    print("Wrong password")



# ==========================================
# DAY 1 COMPLETED
# ==========================================


print("\n===== DAY 1 COMPLETED =====")

print(
    "Variables, data types, input/output and basic programs completed."
)