# ==========================================
# Day 03 - Python Loops
# Topic: for loop, while loop, nested loops
# Project: Number Pattern Generator
# ==========================================


print("===== AI Python Journey - Day 03 =====")
print("Loops Practice Program\n")


# ==========================================
# 1. FOR LOOP BASIC EXAMPLE
# ==========================================

print("1. For Loop Counting")

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


    print(
        "Training Epoch:",
        epochs
    )


    epochs += 1



print("\n===== Day 03 Completed Successfully =====")



print("===== AI Python Journey - Day 03 =====")
print("Loops Practice Program\n")



# ==========================================
# 1. FOR LOOP BASIC EXAMPLE
# ==========================================

# 1. Print numbers 1 to 100
for i in range(1,101):
    print(i)
# 2. Print numbers from 100 to 1
for i in range(100,1):
    print(i)

print("1. For Loop Counting")

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


    print(
        "Training Epoch:",
        epochs
    )


    epochs += 1



print("\n===== Day 03 Completed Successfully =====")
