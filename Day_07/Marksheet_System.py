# Marksheet System using functions

def Calculate_Grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def add_marksheet(marksheets):
    name = input("     Enter Student Name 👤: ").strip()
    father_name = input("     Enter fathers name 👤: ").strip()

    subjects =[
            "English", "Urdu", "Math",
        "Computer", "Islamiat"
              ]

    subject_marks = {}
    total = 0
    for subject in subjects:
        marks = int(input(f"     Enter {subject} marks : "))
        subject_marks[subject] = marks
        total += marks
    maximum_marks = len(subjects) *100
    percentage = (total /maximum_marks) *100
    grade = Calculate_Grade(percentage)

    student ={
        "Name" : name ,
        "Father Name" : father_name,
        "Subject Marks" : subject_marks,
        "Maximum Marks" : maximum_marks,
        "Total Marks" : total,
        "Percentage" : percentage,
        "Grade" : grade
    }

    marksheets.append(student)
    print("        Marksheet Added Successfully 🎉")

def show_marksheet(student):
    print("\n        I➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖I")
    print("        ♦♦♦♦♦♦ STUDENT MARKSHEET ♦♦♦♦♦♦")
    print("          Student Name: ",student["Name"])
    print("          Father Name : ",student["Father Name"])
    print("        ========================================")

    for subject,marks in student["Subject Marks"].items():
        print(f"        {subject}:{marks}/100")
    print("        ========================================")
    print("        Total : ",student["Total Marks"],"/",student["Maximum Marks"])
    print("        Percentage : ",round(student["Percentage"],2),"%")
    print("        Grade : ",student["Grade"])

    print("        ✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️✴️")
    print("\n        I➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖I")
def show_all_marksheets(marksheets):
    for student in marksheets:
        show_marksheet(student)

    if len(marksheets) == 0:
        print("       No marksheets are available")
        return

def search_marksheet(marksheets):
    search_name = input("        Enter name of student to Search : ").strip().lower()
    found = False
    for student in marksheets:    
        if search_name == student["Name"].lower():
            show_marksheet(student)
            found = True
    if not found:
        print("        Marksheet Not Found")


def main():
    marksheets = []
    while True:
        print("\n        ♦♦♦♦♦♦ MARKSHEET SYSTEM ♦♦♦♦♦♦")
        print("          1⃣. ADD MARKSHEET " )
        print("          2⃣. SEARCH MARKSHEET" )
        print("          3⃣. ALL MARKSHEETS" )
        print("          4⃣. EXIT " )

        choice = int(input("        Enter Choice (1-4) : "))
        if choice == 1:
            add_marksheet(marksheets)
        elif choice == 2:
            search_marksheet(marksheets)
        elif choice == 3:
            show_all_marksheets(marksheets)
        elif choice == 4:
            print("        Program Closed")
            break
        else:
            print("        Invalid choice! Select 1,2,3 or 4")

main()
