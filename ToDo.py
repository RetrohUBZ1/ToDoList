f = open("Tasklist.txt", 'r')
task = []

def FileToArray():
    for a in f.readlines():
        task.append(a)

def add_task(tasks):
    task.append(tasks) #Adds input from user into the task array
    print("Task successfully added")

def view_task():
    #print("\n")
    for a in range (len(task)):
        print(task[a])
    print("You have ",len(task)," task(s)")

def remove_task():
    try:
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


def save_task():
    f.close()
    save = open("Tasklist.txt", "w+")
    for a in range(len(task)):
        print(a, task[a])
    for line in task:
        save.writelines(f"{line}")
    save.close()
