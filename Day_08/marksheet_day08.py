# Marksheet System updated using file handling and error handling

import json

FILE = "Marksheets.json"

def load_student_records():
    try:
        with open(FILE , "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("               Marksheet.json invalid, starting with imputy list!")
        return []

def save_student_records(Student_records):
    
    with open(FILE , "w") as f:
        json.dump(Student_records,f,indent = 4)

def grade_calculate(percentage):

    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_marksheet(Student_records):
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("                ===== MARKSHEET DETAIL ===== ")
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    name = input("\n             ☞ Enter Student Name: ")
    father_name = input("\n             ☞ Enter Father Name: ")
    
    subjects = [ "English" , "Math" , "Computer" , "Urdu" , "Islamiyat"]
    subject_marks ={}
    total = 0
    for subject in subjects:
        while True:
            try:
                marks = int(input(f"\n            ↪️ Enter {subject} Marks: ")) 
                if 0<= marks <= 100:
                    subject_marks[subject] = marks
                    total += marks
                    break
                else:
                    print("\n             Enter Marks from 0 to 100!")
            except ValueError:
                print("\n             Please Enter Marks in Numbers")
    maximum_marks = len(subjects) *100
    percentage = (total /maximum_marks)*100
    grade = grade_calculate(percentage)

    student = {
            "Name":name,
            "Father Name":father_name,
            "Subject Marks":subject_marks,
            "Total":total,
            "Maximum Marks":maximum_marks,
            "Percentage":percentage,
            "Grade":grade
            }
    Student_records.append(student)
    save_student_records(Student_records)
    print("\n             Marksheet Added Successfuly 🎉")


def show_marksheet(student):
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("                ((((((  Marksheet Of", student["Name"], ")))))")
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("\n          Name : ",student["Name"].title())
    print("\n          Father Name : ",student["Father Name"].title())
    print("\n        ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️ " )
    for subject,marks in student["Subject Marks"].items():
        print(f"\n          {subject}   :  {marks} / 100")
    print("\n       ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️ " )

    print("\n          Total Marks : ",student["Total"])
    print("\n          Max Marks : ",student["Maximum Marks"])
    print("\n          Percentage : ",round(student["Percentage"],2))
    print("\n          Grade : ",student["Grade"])
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")


def search_marksheet(Student_records):
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("                ===== SEARCH MARKSHEETS ===== ")
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    search_name = input("\n          ↪️ Enter Name to Search Marksheet: ").lower()
    found = False
    for student in Student_records:
        if search_name == student["Name"].lower():
            show_marksheet(student)
            print("\n          Markaheet Found 🎉")
            found = True
        else:
             None

def show_all_marksheets(Student_records):
    print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
    print("                ===== ALL MARKSHEETS ===== ")
    print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ") 
    if len(Student_records) == 0:
        print("\n          No any Markaheet is available !")
    for student in Student_records:
        show_marksheet(student)



Student_records = load_student_records()


def main():
    while True:
   
        print("\n        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")
        print("                ▪️===== MARKSHEET SYSTEM ===== ")
        print("        ⚜️ ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖️➖ ⚜️ ")


        print("\n             1⃣. ADD MARKSHEEET. " )
        print("\n             2⃣. SEARCH MARKSHEET. " )
        print("\n             3⃣. ALL MARKSHEETS. " )
        print("\n             4⃣. EXIT. " ) 

        choice = int(input("\n             ↪️.Enter Choice (1-4): "))
        if choice == 1:
            add_marksheet(Student_records)
        elif choice == 2:
            search_marksheet(Student_records)
        elif choice == 3:
            show_all_marksheets(Student_records)
        elif choice == 4:
            print("\n               Program closed!")
            break
        else:
            print("\n                Invalid Choice")

main()
