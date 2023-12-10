student_list = []
student_grades = {}

while True:
    print('''
    Welcome to this program,
    Type 1 to register students,
    Type 2 to enter the grade,
    Type 3 to list students and their grades,
    Type 4 to exit
    ''')

    user_selection = int(input("Kindly enter your selection: "))

    if user_selection == 1:
        quantity = int(input("How many students are there?: "))
        for _ in range(quantity):
            student_name = input("Enter student name: ")
            student_list.append(student_name)

    elif user_selection == 2:
        if not student_list: 
            print("No students registered. Please register students first.")
        else:
            assignment_name = input("What is the name of the assignment: ")
            total_score = float(input("What is the maximum possible score: "))

            for student in student_list:
                student_score = float(input(f"What is the score for {student}: "))
                student_grades[(student,assignment_name)] = student_score
            print(student_grades)
            print("Grades entered successfully!")
            

    elif user_selection == 3:
        if not student_list:
            print("No students registered. Please register students first.")
        else:
            print("Student Grades:")
            for student in student_list:
                for assignment, score in student_grades.items():
                    if assignment[0] == student:
                        print(f"{student}: {assignment[1]} - Score: {score}")

    elif user_selection == 4:
        break
    else:
        print("Invalid choice. Please select a valid option.")


