page = []
def adding_list():
    a = input("enter the task:")
    page.append(a)
    return page

def view_list():
    print(page)
    return page

def removing():
    page.remove(d)
    return page


while True :
    task = input("enter the task (add,view,remove):")
    if(task == "add"):
        adding_list()
    elif(task == "view"):
        view_list()
    elif(task == "remove"):
        d = input("enter the task to remove:")
        if d in page:
            removing()
        elif( d not in page):
            print(page)
    else:
        print("wrong spelling")
    g = input("do you want to use to do list again (yes or no):")
    if g != "yes":
        break