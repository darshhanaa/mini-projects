students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    students[roll] = {
        "name": name,
        "age": age,
        "marks": marks
    }

    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    for roll, info in students.items():
        print("\nRoll:", roll)
        print("Name:", info["name"])
        print("Age:", info["age"])
        print("Marks:", info["marks"])

def search_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")
def delete_student():
    roll = input("Enter roll number: ")

    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
