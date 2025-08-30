# adding tasks
tasks = []
def add_task(tasks):
    while True:
        a = input("Add Task : ")
        tasks.append(a)
        while True:
            yn = input("Do You Want To Add Another Task?(Yes/No) : ")
            if yn.lower().strip()=="yes":
                add_task(tasks)
            elif yn.lower().strip()=="no":
                exitview(tasks)
            else:
                print("Please Enter a Valid Response")
                break
# exit and view tasks
def exitview(tasks):    
    r = input("Do You Want To Exit And View Your Tasks?(Yes/No) : ")
    if r.lower().strip()=="yes":
        view_tasks(tasks)
    elif r.lower().strip()=="no":
        add_task(tasks)

# view tasks2
def view_tasks2(tasks):
    for i in range(len(tasks)):
        print("Task",i+1,tasks[i].upper())        

# view tasks
def view_tasks(tasks):
    while True:
            b = input("Do You Want To View Your Tasks(Yes/No) : ")
            if b.lower().strip()=="yes":
                for i in range(len(tasks)):
                    print("Task",i+1,tasks[i].upper())
            elif b.lower().strip()=="no":
                del_tasks(tasks)
            else:
                print("Please Enter a Valid Response")
                continue

def del_tasks(tasks):
    for j in range(len(tasks)):
        c = input("Have You Completed Your Task(Yes/No) : ")
        if c.lower().strip()=="yes":
            t = int(input("Which Task Have You Completed(Enter the Task Number) : "))
            for i in range(len(tasks)):
                if t-1==i:
                    del tasks[i]
                    print("Task Completed")
        elif c.lower().strip()=="no":
            print("No Worries,You've Got This-Just Keep At It")
        n = input("Do You Want To View Your Tasks(Yes/No) : ")
        if n.lower().strip()=="yes":
            view_tasks2(tasks)
        if len(tasks)==0:
            f = input("There Are No Tasks, Do You Want To Add One?(Yes/No) : ")
            if f.lower().strip()=="yes":
                        add_task(tasks)
            elif f.lower().strip()=="no":
                h = input("Do You Want To Close The Program?(Type Close/No)")
                if h.lower().strip()=="close":
                     quit
                elif h.lower()=="no":
                    view_tasks(tasks)
add_task(tasks)
exitview(tasks)
view_tasks(tasks)  
del_tasks(tasks)