
# Student Management System

students = []


# 1. Add Student
def add_student():

    print("\n===== ADD NEW STUDENT =====")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty!")
        return

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    course = input("Enter Student Course: ").strip()

    if not name or not age.isdigit() or not course:
        print("Please enter valid student details!")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": int(age),
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


# 2. View All Students
def view_students():

    print("\n===== ALL STUDENTS =====")

    if not students:
        print("No student records found!")
        return

    for student in students:

        print("-------------------------")
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


# 3. Search Student
def search_student():

    student_id = input("Enter Student ID to search: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found!")


# 4. Update Student
def update_student():

    student_id = input("Enter Student ID to update: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("Enter new details:")

            name = input("New Name: ").strip()
            age = input("New Age: ").strip()
            course = input("New Course: ").strip()

            if not name or not age.isdigit() or not course:
                print("Invalid details! Update cancelled.")
                return

            student["name"] = name
            student["age"] = int(age)
            student["course"] = course

            print("Student updated successfully!")
            return

    print("Student not found!")


# 5. Delete Student
def delete_student():

    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            print("Student deleted successfully!")
            return

    print("Student not found!")


# Main Menu
def main():

    while True:

        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

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
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
