"""
DAY 2 - IF/ELSE + LOGICAL OPERATORS

Topics:
- if statement
- elif statement
- else statement
- comparison operators
- logical operators
- grade classifier project

"""


# ==========================================
# SECTION 1: BASIC IF STATEMENT
# ==========================================

print("===== BASIC IF =====")


age = 20


if age >= 18:

    print("You are an adult")



# ==========================================
# SECTION 2: IF ELSE
# ==========================================


print("\n===== IF ELSE =====")


marks = 45


if marks >= 50:

    print("You Passed")


else:

    print("You Failed")



# ==========================================
# SECTION 3: IF ELIF ELSE
# ==========================================


print("\n===== IF ELIF ELSE =====")


score = 85


if score >= 90:

    print("Grade A")


elif score >= 80:

    print("Grade B")


elif score >= 70:

    print("Grade C")


else:

    print("Grade F")



# ==========================================
# SECTION 4: COMPARISON OPERATORS
# ==========================================


print("\n===== COMPARISON =====")


x = 10

y = 5



print(x > y)

print(x < y)

print(x == y)

print(x != y)

print(x >= y)

print(x <= y)



# ==========================================
# SECTION 5: LOGICAL OPERATORS
# ==========================================


print("\n===== LOGICAL OPERATORS =====")


student_age = 20


has_card = True



# AND
# Both conditions must be true


if student_age >= 18 and has_card:

    print("Entry allowed")



# OR
# Any one condition can be true


is_admin = False


if is_admin or has_card:

    print("Access granted")



# NOT
# Reverses condition


is_blocked = False


if not is_blocked:

    print("Account active")



# ==========================================
# PROJECT: GRADE CLASSIFIER
# ==========================================


print("\n===== GRADE CLASSIFIER =====")



student_name = input(
    "Enter student name: "
)


marks = float(
    input("Enter marks (0-100): ")
)



if marks < 0 or marks > 100:

    grade = "Invalid marks"



elif marks >= 90:

    grade = "A"



elif marks >= 80:

    grade = "B"



elif marks >= 70:

    grade = "C"



elif marks >= 60:

    grade = "D"



else:

    grade = "F"



print("\n----- RESULT -----")


print(f"Student: {student_name}")

print(f"Marks: {marks}")

print(f"Grade: {grade}")



# ==========================================
# PASS / FAIL SYSTEM
# ==========================================


print("\n===== PASS CHECK =====")


attendance = float(
    input("Enter attendance percentage: ")
)



if marks >= 50 and attendance >= 75:

    print("Result: PASS")


else:

    print("Result: FAIL")



# ==========================================
# DAY 2 COMPLETED
# ==========================================


print("\n===== DAY 2 COMPLETED =====")

print(
    "Learned conditions and logical decision making"
)