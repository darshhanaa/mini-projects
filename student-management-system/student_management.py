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

