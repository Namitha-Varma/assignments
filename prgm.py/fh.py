def add_students():
    s_id=input("enter s_id:")
    name=input("enter student name:")
    course=input("enter course:")

    with open("students.txt","a") as file:
        file.write(f"{s_id},{name},{course}\n")
    print("students added successfully")
    
def view_students():
    try:
        with open("students.txt","r") as file:
            data=file.read()
        if data=="":
            print("data not found")
        else:
            print("sudents list:",data)
    except FileNotFoundError:
        print("students.txt file does not exist.")

def search_student():
    search_id=input("enter student_id:")
    found=False
    with open("students.txt","r") as file:
        for line in file:
            s_id, name, course=line.split(",")
            if s_id==search_id:
                print("\nstudent found")
                print("ID:", s_id)
                print("name:",name)
                print("course:",course)
                found=True
                break
    if not found:
        print("student not found")
    
def students_count():
    try:
        with open("students.txt","r") as file:
            count=len(file.readlines())
        print("Total Students:",count)
    except FileNotFoundError:
        print("students.txt file does not exist.")

def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    try:
        found = False
        records = []
        with open("students.txt", "r") as file:
            for line in file:
                sid = line.strip().split(",")[0]
                if sid != delete_id:
                    records.append(line)
                else:
                    found = True
        with open("students.txt", "w") as file:
            file.writelines(records)
        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found")
    
    except FileNotFoundError:
        print("students.txt file does not exist.")


running=True

while running:
    print("menu\n")
    print("1. add students:")
    print("2. view students:")
    print("3. search student:")
    print("4. student count:")
    print("5. delete student:")
    print("6. Exit:")
    choice=input("enter your choice:")
    if choice=="1":
        add_students()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        students_count()
    elif choice=="5":
        delete_student()
    elif choice=="6":
        print("file exitied")
        running=False
    else:
        print("choose proper choice or try again")   






                


        
  
        




