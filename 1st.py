def calculate_grade(mark):
    if mark >= 90:
        return "S"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

students = {}

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student Name: ")
        mark = int(input("Student Mark: "))
        students[name] = calculate_grade(mark)
        print("Student added successfully")

    elif choice == "2":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "3":
        print("Program terminated")
        break

    else:
        print("Invalid choice")
