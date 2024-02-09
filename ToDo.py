#import numpy as np
f = open("Tasklist.txt", 'r')
task = []
#complete = []

def FileToArray():
    for a in f.readlines():
        task.append(a)
    #if word = 'Line'
#    for b in f.readlines():
 #       complete.append(b)

def add_task(tasks):
    #print("\n")
    task.append(tasks) #Adds input from user into the task array
    print("Task successfully added")

def view_task():
    #print("\n")
    for a in range (len(task)):
        print(task[a])
    print("You have ",len(task)," task(s)")

def remove_task():
    try:
        '''choice = int(input("\n Would you like to remove tasks from complete(1) or not complete(2)\n"))
        if choice == 1:
            if len(complete) > 0: #Checks to see if the length of the list has anything in it to begin with
                for a in range(len(complete)):
                    print(a, task[a])
                    index = int(input("Which completed task would you like to remove?\n"))
                    #if a in range(len(task)):
                    task.pop(index)
                    print("task successfully removed\n")
                    #else:
                     #   print("Line is out of bounds")
            else:
                print("No tasks to remove")

        elif choice == 2:
'''
        if len(task) > 0: #Checks to see if the length of the list has anything in it to begin with
              for b in range(len(task)):
                print(b,task[b])
              index = int(input("Which task would you like to remove?\n"))
              task.pop(index)
                #if b in range(len(task)):
              print("task successfully removed")
                #else:
                 #   print("Line is out of bounds")
    except:
        print("Line is out of bounds")
        save_task()



def complete_task():
    for a in range(len(task)):
        print(a, task[a])
    comp = int(input("Which task would you like to mark as complete?"))
    print(task[comp].strip() + " has been completed")
    task[comp] = task[comp].strip() + ' COMPLETE\n'
    for a in task:
        print(a)
    #task[comp] = newcomp
    #complete.append(task[comp])
    #task.pop(comp)


def save_task():
    f.close()
    save = open("Tasklist.txt", "w+")
    for a in range(len(task)):
        print(a, task[a])
    for line in task:
        save.writelines(f"{line}")
    '''
        save.writelines(task[a])
    if len(complete) > 0:
        for a in range(len(complete)):
            save.writelines("\n Complete \n"+complete[a]+"\n")
'''
    save.close()
