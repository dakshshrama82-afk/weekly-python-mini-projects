#main billing book and total exp defien

billbook = {}
bill_log = []
totalmoney = []

#printing wellcom and option menu

print("wellcome to CLI:\n","choose the menu option:")
menu = ["adding exp","view exp","total","remove exp"]
print(menu)

#making a function for adding expense

def adding_exp():
    a = float(input("enter the value: "))
    while a < 0:
        print("wrong value")
        a = float(input("enter the value: "))
    b = input("enter the catagory :").lower()
    billbook[b] = a
    done = input("done adding all exp(yes/no):")
    if done == "yes":
        totalmoney.append(a)
    else:
        adding_exp()

# making a function for viewing billbook

def view_exp():
    if billbook == {}:
        print("nothing found")
    else:
        print(billbook)

#making a function for total expense

def total_exp():
    if totalmoney == []:
        print("nothing found")
    else:
        print(sum(totalmoney))

#making a function for removing exp

def removing_exp():
    if billbook == {}:
        print("nothing in it")
    else:
        print(billbook)
        remove = input("enter the task to remove:")
        billbook.pop(remove)
        totalmoney.append(billbook)
        print(billbook)

# looping all function (also you can call it the heart of this program)

while True:
    user_task = input("enter the task:").lower()
    if user_task == "adding" or user_task == "adding exp":
        adding_exp()
    elif user_task == "view" or user_task == "view exp":
        view_exp()
    elif user_task == "total_mony" or user_task == "total":
        total_exp()
    elif user_task == "removing":
        removing_exp()
    elif user_task == "exit":
        break
    else:
        print("option does not found")


