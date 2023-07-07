import json

def main():
    grades = {}
    with open("grades.txt", "r") as file:
        grades = json.load(file)

    while True:
        print("1. Create a student name and grade")
        print("2. Ask for a grade, given the full name of the student")
        print("3. Edit a grade")
        print("4. Delete a grade")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the student's name: ")
            grade = input("Enter the student's grade: ")
            grades[name] = grade
        elif choice == "2":
            name = input("Enter the student's name: ")
            if name in grades:
                print(f"{name}'s grade is {grades[name]}")
            else:
                print(f"{name} does not exist")
        elif choice == "3":
            name = input("Enter the student's name: ")
            if name in grades:
                grade = input("Enter the student's grade: ")
                grades[name] = grade
            else:
                print(f"{name} does not exist")
        elif choice == "4":
            name = input("Enter the student's name: ")
            if name in grades:
                del grades[name]
            else:
                print(f"{name} does not exist")
        elif choice == "5":
            break
        else:
            print("Invalid choice")

        print()
        with open("grades.txt", "w") as file:
            json.dump(grades, file)

main()