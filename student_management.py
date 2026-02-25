import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("Student already exists!")
            return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print("\n--------------------")
        print(f"Roll: {student['roll']}")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Grade: {student['grade']}")
        print("--------------------")


def search_student():
    students = load_students()
    roll = input("Enter Roll to search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found:")
            print(student)
            return

    print("Student not found.")


def update_student():
    students = load_students()
    roll = input("Enter Roll to update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["marks"] = float(input("Enter new marks: "))

            if student["marks"] >= 90:
                student["grade"] = "A"
            elif student["marks"] >= 75:
                student["grade"] = "B"
            elif student["marks"] >= 50:
                student["grade"] = "C"
            else:
                student["grade"] = "Fail"

            save_students(students)
            print("Updated successfully!")
            return

    print("Student not found.")


def delete_student():
    students = load_students()
    roll = input("Enter Roll to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Deleted successfully!")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()