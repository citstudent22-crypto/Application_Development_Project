import os

class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")

        student = {
            "Roll": roll,
            "Name": name,
            "Course": course
        }

        self.students.append(student)
        print("Student Added Successfully!")

    def view_students(self):
        if not self.students:
            print("No Students Found!")
            return

        print("\n===== STUDENT RECORDS =====")
        for student in self.students:
            print(f"Roll: {student['Roll']}")
            print(f"Name: {student['Name']}")
            print(f"Course: {student['Course']}")
            print("-" * 30)

    def search_student(self):
        roll = input("Enter Roll Number to Search: ")

        for student in self.students:
            if student["Roll"] == roll:
                print("\nStudent Found!")
                print(student)
                return

        print("Student Not Found!")

    def delete_student(self):
        roll = input("Enter Roll Number to Delete: ")

        for student in self.students:
            if student["Roll"] == roll:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def menu(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.delete_student()

            elif choice == "5":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")

system = StudentManagementSystem()
system.menu()