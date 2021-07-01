tasks = []

def display_menu():
    print('''
    MENU
    a --- Enter New Task
    b --- View All Tasks
    c --- Remove Task
    --------------------
''')

def enter_task():
    print("Enter New Task")
    print("----------")
    tasks.append(input("Enter task >_ "))

def view_tasks():
    print("View Tasks")
    print("----------")
    if len(tasks) < 1:
        print("All tasks complete!")
    else:
        show_tasks()

    print("Press enter to continue...")
    input()

def show_tasks():
    for i in range(len(tasks)):
            print(str(i+1) + ": " + tasks[i])

def remove_task():
    print("Delete Task")
    print("----------")
    show_tasks()
    choice = int(input("Enter number to remove"))
    if choice <= len(tasks):
        print("Congratulations on completing " + tasks[choice - 1])
        del tasks[choice - 1]
        
    

while True:
    display_menu()
    choice = input("Enter a choice >_ ")
    if choice == "a":
        enter_task()
    elif choice == "b":
        view_tasks()
    elif choice == "c":
        remove_task()
    else:
        print("Invalid option! Press enter to continue")
        input()
