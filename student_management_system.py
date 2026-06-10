students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        students.append([name, roll])
        print("Student added successfully!")

    elif choice == '2':
        print("\nStudent Records:")
        for s in students:
            print("Name:", s[0], "| Roll No:", s[1])

    elif choice == '3':
        roll = input("Enter roll number to search: ")
        found = False
        for s in students:
            if s[1] == roll:
                print("Name:", s[0], "| Roll No:", s[1])
                found = True
                break
        if not found:
            print("Student not found!")

    elif choice == '4':
        roll = input("Enter roll number to delete: ")
        for s in students:
            if s[1] == roll:
                students.remove(s)
                print("Student deleted!")
                break

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")