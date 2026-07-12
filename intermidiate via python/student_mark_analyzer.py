students = []
while True:
    print("\n--STUDENT MARK ANALYSER---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Find Topper")
    print("6. Highest And Lowest Marks")
    print("7. Delete Student")
    print("8. Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        students = input("Enter the student name: ")
        Maths_Marks = float(input("Enter your maths Marks: "))
        Physics_Marks = float(input("Enter Your Physics Marks: "))
        Chemistry_Marks = float(input("Enter Your Chemistry Marks: "))
        students = {"Name": students,
                    "Maths_Marks": Maths_Marks,
                    "Physics_Marks": Physics_Marks,
                    "Chemistry_Marks": Chemistry_Marks}