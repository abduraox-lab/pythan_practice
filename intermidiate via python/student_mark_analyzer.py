students = []

while True:
    print("\n--- STUDENT MARKS ANALYZER ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Find Topper")
    print("6. Highest & Lowest Marks")
    print("7. Delete Student")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            continue
        maths = float(input("Enter Maths marks: "))
        physics = float(input("Enter Physics marks: "))
        chemistry = float(input("Enter Chemistry marks: "))
        students.append({
            "Name": name,
            "Maths": maths,
            "Physics": physics,
            "Chemistry": chemistry
        })
        print(f"Student '{name}' added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print(f"\n{'Name':<20} {'Maths':<8} {'Physics':<8} {'Chemistry':<8} {'Average':<8}")
            print("-" * 52)
            for s in students:
                avg = (s["Maths"] + s["Physics"] + s["Chemistry"]) / 3
                print(f"{s['Name']:<20} {s['Maths']:<8} {s['Physics']:<8} {s['Chemistry']:<8} {avg:<8.2f}")

    elif choice == "3":
        search_name = input("Enter student name to search: ").strip().lower()
        found = [s for s in students if s["Name"].lower() == search_name]
        if found:
            s = found[0]
            avg = (s["Maths"] + s["Physics"] + s["Chemistry"]) / 3
            print(f"Name: {s['Name']}")
            print(f"Maths: {s['Maths']}, Physics: {s['Physics']}, Chemistry: {s['Chemistry']}")
            print(f"Average: {avg:.2f}")
        else:
            print("Student not found.")

    elif choice == "4":
        if not students:
            print("No students to calculate average.")
        else:
            total_maths = sum(s["Maths"] for s in students)
            total_physics = sum(s["Physics"] for s in students)
            total_chemistry = sum(s["Chemistry"] for s in students)
            count = len(students)
            print(f"Class Average:")
            print(f"Maths: {total_maths / count:.2f}")
            print(f"Physics: {total_physics / count:.2f}")
            print(f"Chemistry: {total_chemistry / count:.2f}")
            overall = (total_maths + total_physics + total_chemistry) / (count * 3)
            print(f"Overall Average: {overall:.2f}")

    elif choice == "5":
        if not students:
            print("No students to find topper.")
        else:
            topper = max(students, key=lambda s: (s["Maths"] + s["Physics"] + s["Chemistry"]) / 3)
            avg = (topper["Maths"] + topper["Physics"] + topper["Chemistry"]) / 3
            print(f"Topper: {topper['Name']} with an average of {avg:.2f}")

    elif choice == "6":
        if not students:
            print("No students to analyze.")
        else:
            for subject in ["Maths", "Physics", "Chemistry"]:
                marks = [s[subject] for s in students]
                highest = max(marks)
                lowest = min(marks)
                h_students = [s["Name"] for s in students if s[subject] == highest]
                l_students = [s["Name"] for s in students if s[subject] == lowest]
                print(f"{subject}: Highest = {highest} ({', '.join(h_students)}), Lowest = {lowest} ({', '.join(l_students)})")

    elif choice == "7":
        del_name = input("Enter student name to delete: ").strip().lower()
        for i, s in enumerate(students):
            if s["Name"].lower() == del_name:
                del students[i]
                print(f"Student '{s['Name']}' deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "8":
        print("Exiting Student Marks Analyzer. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 8.")
