# ==========================================
# Student List Manager
# Topic: Python Lists Practice
# ==========================================


students = []


# Function to add student
def add_student():

    name = input("Enter student name: ")

    students.append(name)

    print(f"{name} added successfully!")



# Function to view students
def view_students():

    if len(students) == 0:

        print("No students available.")

    else:

        print("\n===== Student List =====")

        for index, student in enumerate(students):

            print(f"{index + 1}. {student}")



# Function to remove student
def remove_student():

    name = input("Enter student name to remove: ")

    if name in students:

        students.remove(name)

        print(f"{name} removed successfully!")

    else:

        print("Student not found.")



# Function to search student
def search_student():

    name = input("Enter student name to search: ")

    if name in students:

        print(f"{name} exists in the list.")

    else:

        print("Student not found.")



# Function to update student
def update_student():

    old_name = input("Enter current student name: ")

    if old_name in students:

        new_name = input("Enter new student name: ")

        index = students.index(old_name)

        students[index] = new_name

        print("Student updated successfully!")

    else:

        print("Student not found.")



# Main program

while True:

    print("\n==============================")
    print("     Student List Manager")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Count Students")
    print("7. Exit")


    choice = input("Enter your choice: ")



    if choice == "1":

        add_student()



    elif choice == "2":

        view_students()



    elif choice == "3":

        remove_student()



    elif choice == "4":

        search_student()



    elif choice == "5":

        update_student()



    elif choice == "6":

        print(f"Total students: {len(students)}")



    elif choice == "7":

        print("Program closed.")

        break



    else:

        print("Invalid choice. Try again.")