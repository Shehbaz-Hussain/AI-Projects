# ==========================================
# Day 03 - Python Loops
# Topic: for loop, while loop, nested loops
# Project: Number Pattern Generator
# ==========================================


print("===== AI Python Journey =====")
print("Loops Practice Program\n")


# ==========================================
# 1. FOR LOOP BASIC EXAMPLE
# ==========================================

print("1. For Loop Counting")


# Print numbers 1 to 100
for i in range(1, 101):
    print(i)


print()


# Print numbers 100 to 1
for i in range(100, 0, -1):
    print(i)


print()


# Simple counting example
for number in range(1, 6):
    print(number)


print()


# ==========================================
# 2. LOOP THROUGH LIST
# ==========================================

print("2. Loop Through AI Topics")


ai_topics = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "NLP"
]


for topic in ai_topics:
    print(topic)


print()


# ==========================================
# 3. WHILE LOOP EXAMPLE
# ==========================================

print("3. While Loop Example")


count = 1


while count <= 5:

    print("AI Engineering Step:", count)

    count += 1


print()


# ==========================================
# 4. USER INPUT NUMBER PATTERN
# ==========================================

print("4. Number Pattern Generator")


rows = int(input("Enter number of rows: "))


for i in range(1, rows + 1):

    for j in range(1, i + 1):

        print(j, end=" ")

    print()


print()


# ==========================================
# 5. STAR PATTERN
# ==========================================


print("5. Star Pattern")


for i in range(1, rows + 1):

    for j in range(i):

        print("*", end="")

    print()


print()


# ==========================================
# 6. REVERSE PATTERN
# ==========================================


print("6. Reverse Pattern")


for i in range(rows, 0, -1):

    for j in range(i):

        print("*", end="")

    print()


print()


# ==========================================
# 7. MULTIPLICATION TABLE GENERATOR
# ==========================================


print("7. Multiplication Table")


number = int(input("Enter number for table: "))


for i in range(1, 11):

    result = number * i

    print(number, "x", i, "=", result)


print()


# ==========================================
# 8. EVEN NUMBER GENERATOR
# ==========================================


print("8. Even Numbers")


for i in range(1, 21):

    if i % 2 == 0:

        print(i)


print()


# ==========================================
# 9. SUM USING LOOP
# ==========================================


print("9. Sum of Numbers")


total = 0


for i in range(1, 11):

    total += i


print("Total =", total)


print()


# ==========================================
# 10. NESTED LOOP MATRIX EXAMPLE
# ==========================================


print("10. Matrix Pattern")


for row in range(3):

    for column in range(3):

        print("1", end=" ")

    print()


print()


# ==========================================
# 11. AI DATA PROCESSING EXAMPLE
# ==========================================


print("11. AI Prediction Processing")


predictions = [
    0.91,
    0.45,
    0.78,
    0.20,
    0.88
]


for prediction in predictions:


    if prediction >= 0.5:

        print(
            prediction,
            "=> Positive Prediction"
        )


    else:

        print(
            prediction,
            "=> Negative Prediction"
        )


print()


# ==========================================
# 12. SIMPLE MODEL TRAINING SIMULATION
# ==========================================


print("12. AI Training Simulation")


epochs = 1


while epochs <= 5:

    print("Training Epoch:", epochs)

    epochs += 1



print("\n===== Day 03 Completed Successfully =====")

"""
Day 03 - Advanced Loop Practice

Topics:
- Nested loops
- Pattern generation
- Prime numbers
- Fibonacci
- Data processing
- AI-style calculations
"""


# ==========================================
# Task 1: Number Triangle With Row Sum
# ==========================================

print("Task 1: Number Triangle With Sum")

rows = 4

for i in range(1, rows + 1):

    row_sum = 0

    for j in range(1, i + 1):

        print(j, end=" ")

        row_sum += j

    print(" | Row Sum =", row_sum)


print()


# ==========================================
# Task 2: Prime Number Generator
# ==========================================

print("Task 2: Prime Numbers 1-100")


for number in range(2, 101):

    is_prime = True

    for i in range(2, number):

        if number % i == 0:

            is_prime = False
            break


    if is_prime:

        print(number, end=" ")


print("\n")


# ==========================================
# Task 3: Reverse Number Pattern
# ==========================================

print("Task 3: Reverse Pattern")


rows = 5


for i in range(rows, 0, -1):

    for j in range(1, i + 1):

        print(j, end="")

    print()


print()


# ==========================================
# Task 4: Diamond Pattern
# ==========================================

print("Task 4: Diamond Pattern")


n = 5


for i in range(1, n + 1):

    print(" " * (n-i), end="")

    print("*" * (2*i-1))


for i in range(n-1, 0, -1):

    print(" " * (n-i), end="")

    print("*" * (2*i-1))


print()


# ==========================================
# Task 5: Pascal Triangle
# ==========================================

print("Task 5: Pascal Triangle")


rows = 5


for i in range(rows):

    number = 1

    print(" " * (rows-i), end="")


    for j in range(i+1):

        print(number, end=" ")

        number = number * (i-j) // (j+1)


    print()


print()


# ==========================================
# Task 6: Fibonacci Sequence
# ==========================================

print("Task 6: Fibonacci")


a = 0
b = 1


for i in range(20):

    print(a, end=" ")

    next_number = a + b

    a = b

    b = next_number


print("\n")


# ==========================================
# Task 7: Dataset Analyzer
# ==========================================

print("Task 7: Dataset Analyzer")


data = [12,45,67,23,89,34,90]


maximum = data[0]

minimum = data[0]

total = 0


for value in data:


    if value > maximum:

        maximum = value


    if value < minimum:

        minimum = value


    total += value



average = total / len(data)


above_average = 0


for value in data:

    if value > average:

        above_average += 1



print("Maximum:", maximum)

print("Minimum:", minimum)

print("Average:", average)

print("Above Average Count:", above_average)


print()


# ==========================================
# Task 8: Model Accuracy Calculator
# ==========================================

print("Task 8: AI Accuracy Calculator")


predictions = [1,0,1,1,0]

actual = [1,1,1,0,0]


correct = 0


for i in range(len(predictions)):


    if predictions[i] == actual[i]:

        correct += 1



accuracy = (correct / len(predictions)) * 100


print("Accuracy =", accuracy, "%")


print()


# ==========================================
# Task 9: Matrix Addition
# ==========================================

print("Task 9: Matrix Addition")


A = [
    [1,2],
    [3,4]
]


B = [
    [5,6],
    [7,8]
]


result = []


for i in range(len(A)):

    row = []


    for j in range(len(A[i])):

        row.append(A[i][j] + B[i][j])


    result.append(row)



for row in result:

    print(row)


print()


# ==========================================
# Task 10: Neural Network Simulation
# ==========================================

print("Task 10: Neural Network Calculation")


inputs = [2,3,4]

weights = [0.5,0.2,0.1]


output = 0


for i in range(len(inputs)):

    output += inputs[i] * weights[i]



print("Model Output =", output)


print()


print("===== All Day 3 Advanced Tasks Completed =====")