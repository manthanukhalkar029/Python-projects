students ={}

while True:
    print("\n-----STUDENT MANAGER SYSTEM-----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = int(input("Enter your choice:"))

    #add student
    if choice ==1:
        name = input("Enter your name:")
        marks = int(input("Enter your marks:"))
        students[name] = marks
        print(f'{name} Successfully Added!!')

    #View Student
    elif choice ==2:
        if not students:
            print("NO student found!")
        else:
            for name , marks in students.items():
                print(f'{name} : {marks}')

    #check result 
    elif choice == 3:
        name = input("Enter student name:")

        if name in students:
            marks = students[name]
            if marks >= 40:
                print("PASS !!!")
            else:
                print("FAIL")
        else:
            print('Student Not Found')

    elif choice == 4:
        print("Exiting.....")
        break

    else:
        print("In-valid Input")




     