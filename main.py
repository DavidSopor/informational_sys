from information_system import InformationSystem
from personal import Teacher 

def print_menu():
    print("\n*******************************************")
    print("Welcome in system")
    print("Choose please:")
    print("\t[0] To add teacher")
    print("\t[1] To add curse")
    print("\t[2] To add student")
    print("\t[3] To add cleaner")
    print("\t[4] For the list of curses")
    print("\t[5] For the list of students")
    print("\t[6] For the list of teachers")
    print("\t[7] For the list of cleaners")
    print("\t[8] To END system")

in_sys = InformationSystem(
    teachers=[
        Teacher("Ladislav", "Hrubý", "Ing"),
        Teacher("Michal", "Hucko", "Ing")
    ]
)

while True:
    print_menu()
    try:
        menu_choice=int(input("Menu choice: "))
        if menu_choice<0 or menu_choice >=9:
            raise Exception("Wrong menu choice")
    except Exception as e:
        print(e)
        print("Please choose valid menu choice")
        continue
    if menu_choice ==8:
        print("Good bye")
        break
    elif menu_choice == 0:
        in_sys.create_teacher()
    elif menu_choice == 1:
        in_sys.create_course()
    elif menu_choice == 2:
        in_sys.create_student()
    elif menu_choice == 3:
        in_sys.create_cleaner()
    elif menu_choice == 4:
        print("Courses are")
        for course in in_sys.courses:
            print(course)
    elif menu_choice == 5:
        print("Students are")
        for student in in_sys.students:
            print(student)
    elif menu_choice == 6:
        print("Teachers are")
        for teacher in in_sys.teachers:
            print(teacher)
    elif menu_choice == 7:
        print("Cleaners are")
        for cleaner in in_sys.cleaners:
            print(cleaner)