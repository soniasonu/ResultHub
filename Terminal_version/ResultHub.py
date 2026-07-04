student = {}

while True:
    print("\n--------Student Result Manager----------")
    print("1.Add Students.")
    print("2.View STudents.")
    print("3.Chack Result.")
    print("4.Passed students.")
    print("5.Exit.")

    choice = int(input("Enter name: "))

    if choice == 1:
        name = input("Enter name: ")
        mark = int(input("Enter mark: "))
        student[name] = mark
        print(f"{name} successfully Added!")
        

    elif choice == 2:
        if not student:
            print("student not found.")
        else:
            for name, mark in student.items():
                print(name, ":", mark)


    elif choice == 3:
        name = input("Enter name: ")
        mark = student[name]

        if mark >= 40 :
            print("Pass")
        else:
            print("Fail")


    elif choice == 4:
        print("Passed students: ")
        for name, mark in student.items():
            if mark >= 40:
                print(f"{name}-{mark}")


    elif choice == 5:
        print("Goodbye")
    else:
        print("Invalid input!")