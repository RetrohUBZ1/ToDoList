# This is a sample Python script.
#from To
#from To-Do_List_App import add_task
from ToDo import add_task
from ToDo import view_task
from ToDo import remove_task
from ToDo import save_task
from ToDo import FileToArray
from ToDo import complete_task

#To-Do_List_App import add_task
#import To-Do List App
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Greetings User\n")
FileToArray()

while True:
    print(" Add task (1)\n View task(s)(2)\n Remove task(s) (3)\n Complete task(s) (4)\n Any other number to Save task(s)")
    num = int(input("Choose a task you wish to perform\n"))
    match num:
        case 1:
            task = input("Please add a task")
            add_task(task)
            print("\n"),
        case 2:
            view_task()
            print("\n"),
        case 3:
            remove_task()
            print("\n"),
        case 4:
            complete_task()
            print("\n"),
        case _:
            print("Saving tasks")
            save_task()
            exit()

'''while True:
    #num = int(input("Choose a task you wish to perform\n"))
    if num == 1:
        task = input("Please add a task")
        add_task(task)

    elif num == 2:
        view_task()

    else:
        exit()'''