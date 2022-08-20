"""
@author: Chen-Tung Chu
@date: 2022-08-09
"""

import os


filename = "students.txt"


def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            find_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            change_student_status()
        elif choice == 5:
            show_all_student_status()
        elif choice == 6:
            show_standing()
        elif choice == 7:
            show_total_students()
        elif choice == 0:
            second_choice = input("Are you sure you want to exit? (y/n): ")
            if second_choice in ("y", "Y"):
                print("Thank you for using our system!")
                break
            else:
                continue
        else:
            print("Invalid choice!")
            continue

def menu():
    print("=========================Student System=========================")
    print("------------------------------Menu------------------------------")
    print("\t\t\t1. Add student")
    print("\t\t\t2. Find student")
    print("\t\t\t3. Delete student")
    print("\t\t\t4. Change student status")
    print("\t\t\t5. Show all student status")
    print("\t\t\t6. Show standing")
    print("\t\t\t7. Show total students")
    print("\t\t\t0. Exit")
    print("=================================================================")



def add_student():
    while True:
        std_list = []
        std_id = input("Enter 5-digit student ID: ")
        if len(std_id) != 5:
            print("Invalid student ID!")
            continue
        std_name = input("Enter student name: ")
        if not std_name:
            print("Invalid student name!")
            continue
        std_gender = input("Enter student gender: ")
        if std_gender not in ("M", "F", "m", "f"):
            print("Invalid gender!")
            continue
        std_gender = std_gender.upper()

        try:
            english_score = int(input("Enter student English score: "))
            math_score = int(input("Enter student Math score: "))
            science_score = int(input("Enter student Science score: "))
            if any([score is None or score < 0 or score > 100 for score in [english_score, math_score, science_score]]):
                raise
            score_avg = round((english_score + math_score + science_score) / 3, 2)
        except:
            print("Invalid score!")
            continue
        
        std = {"Student Id": std_id, "Name": std_name, "Gender": std_gender, "English": english_score, "Math": math_score, "Science": science_score, "Average": score_avg}
        std_list.append(std)

        save(std_list)
        print("Student added successfully!")
        answer = input("Do you want to add another student? (y/n): ")
        if answer in ("y", "Y"):
            continue    
        else:
            break


def save(std_list):
    with open("students.txt", "a", encoding='UTF-8') as f:
        for std in std_list:
            f.write(str(std) + "\n")
   

def delete_student():
    while True:
        std_id = input("Enter student ID: ")
        if len(std_id) != 5:
            print("Invalid student ID!")
            continue

        if os.path.exists(filename):
            with open("students.txt", "r", encoding='UTF-8') as f:
                std_list = f.readlines()
                
            if std_list:
                found_del = False
                with open(filename, "w", encoding='UTF-8') as wf:
                    for std in std_list:
                        d = dict(eval(std))
                        if d["Student Id"] == std_id:
                            found_del = True
                        else:
                            wf.write(str(d) + "\n")
                    if found_del:
                        print(f"Student Id {std_id} deleted successfully!\n")
                    else:
                        print(f"Student Id {std_id} not found!")
                        continue
            else:
                print("Student list is empty!\n")
                break

            show()      # show students after deletion
        answer = input("Do you want to delete another student? (y/n): ")
        if answer in ("y", "Y"):
            continue    
        else:
            break


def show():
    if os.path.exists(filename):
        with open(filename, "r", encoding='UTF-8') as f:
            std_list = f.readlines()
            if std_list:
                print("Current students:")
                for std in std_list:
                    d = dict(eval(std))
                    print(d)
                print("\n")
            else:
                print("Student list is empty!\n")
    else:
        print("Student list is empty!\n")


def find_student():
    student_query = []
    while True:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("Enter search mode (1. ID, 2. Name): ")
            if mode == "1":
                id = input("Enter student ID: ")
                if len(id) != 5:
                    print("Invalid student ID!")
                    continue
            elif mode == "2":
                name = input("Enter student name: ")
                if not name:
                    print("Invalid student name!")
                    continue
            else:
                print("Invalid search mode!")
                continue

            with open(filename, "r", encoding='UTF-8') as f:
                std = f.readlines()
                for s in std:
                    d = dict(eval(s))
                    if d["Student Id"] == id or d["Name"] == name:
                        student_query.append(d)
            
            show_std(student_query)
            student_query.clear()

            answer = input("Do you want to find another student? (y/n): ")
            if answer in ("y", "Y"):
                continue
            else:
                break


def show_std(student_query):
    if student_query:
        format_title = '{:^8}\t{:^10}\t{:^6}\t\t{:^7}\t\t{:^6}\t\t{:^8}\t{:^8}'
        print(format_title.format("ID", "Name", "Gender", "English", "Math", "Science", "Average"))
        
        format_data = '{:^8}\t{:^10}\t{:^6}\t\t{:^7}\t\t{:^6}\t\t{:^8}\t{:^8}'
        for std in student_query:
            print(format_data.format(std["Student Id"], std["Name"], std["Gender"], std["English"], std["Math"], std["Science"], std["Average"]))
        print("\n")
    else:
        print("No student found!\n")


def change_student_status():
    show()
    if os.path.exists(filename):
        with open(filename, "r", encoding='UTF-8') as f:
            std_list = f.readlines()
    else:
        return
    
    std_id = input("Enter student ID: ")
    with open(filename, "w", encoding='UTF-8') as wf:
        for std in std_list:
            d = dict(eval(std))
            if d["Student Id"] == std_id:
                while True:
                    try:
                        d['Name'] = input("Enter student name: ")
                        if not d['Name']:
                            raise
                        d['Gender'] = input("Enter student gender: ")
                        if d["Gender"] not in ("M", "F", "m", "f"):
                            raise
                        d['English'] = int(input("Enter student English score: "))
                        d['Math'] = int(input("Enter student Math score: "))
                        d['Science'] = int(input("Enter student Science score: "))
                        if any([score is None or score < 0 or score > 100 for score in [d['English'], d['Math'], d['Science']]]):
                            raise
                        d['Average'] = round((d['English'] + d['Math'] + d['Science']) / 3, 2)
                    except:
                        print("Invalid score!")
                    else:
                        break

                wf.write(str(d) + "\n")
                print("Student status changed successfully!")
            else:
                wf.write(str(d) + "\n")

        answer = input("Do you want to change another student status? (y/n): ")
        if answer in ("y", "Y"):
            change_student_status()
        



def show_standing():
    show()
    if os.path.exists(filename):
        with open(filename, "r", encoding='UTF-8') as f:
            std_list = f.readlines()
        std_new = []
        for std in std_list:
            d = dict(eval(std))
            std_new.append(d)
    else:
        return

    mode = int(input("Which subject do you want to sort by? (1. English, 2. Math, 3. Science, 4. Average): "))
    mode_index = {1: "English", 2: "Math", 3: "Science", 4: "Average"}
    if mode not in range(1, 5):
        print("Invalid option!")
        show_standing()
    else:
        order = int(input("Which order do you want to sort in? (1. ascending, 2. descending): ")) - 1
        if order not in range(2):
            print("Invalid option!")
            show_standing()
        else:
            if mode == 1:
                std_new.sort(key=lambda x: x["English"], reverse=bool(order))
            elif mode == 2:
                std_new.sort(key=lambda x: x["Math"], reverse=bool(order))
            elif mode == 3:
                std_new.sort(key=lambda x: x["Science"], reverse=bool(order))
            elif mode == 4:
                std_new.sort(key=lambda x: x["Average"], reverse=bool(order))
            print(f"\nStudents sorted by {mode_index[mode]} in {'descending' if order else 'ascending'} order:")
            show_std(std_new)
            


def show_total_students():
    if os.path.exists(filename):
        with open(filename, "r", encoding='UTF-8') as f:
            std_list = f.readlines()
            if std_list:
                print(f"Total students: {len(std_list)}\n")
            else:
                print("Student list is empty!\n")
    else:
        print("Student list is empty!\n")


def show_all_student_status():
    std_list = []
    if os.path.exists(filename):
        with open(filename, "r", encoding='UTF-8') as f:
            std = f.readlines()
            for s in std:
                std_list.append(eval(s))
            if std_list:
                print("All students:")
                show_std(std_list)
            print("\n")
    else:
        print("Student list is empty!\n")



if __name__ == "__main__":
    main()
