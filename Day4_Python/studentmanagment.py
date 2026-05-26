students = []

while True:
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:

        name = input("Enter student name:")
        age = int(input("Enter student age:"))
        course = input("Enter student course:")

        student = { "name": name, "age": age, "course": course}
        students.append(student)

        print("Student added successfully")

    elif choice == 2:

        if len(students)==0:
            print("No student records found.")
        else: 
            print("\nStudent Records:")
            for s in students:
                print("Name:", s["name"], "| Age:", s["age"], "| Course:", s["course"])

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")