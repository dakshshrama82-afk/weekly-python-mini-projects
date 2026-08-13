billbook = {}
totalexpens = []
totalmoney = []
print("wellcome to CLI:\n","choose the menu option:")
menu = ["adding exp","view exp","total","remove exp"]
print(menu)
while True:
    task = input("enter the perpouse: ")
    if task == "adding exp":
        a = int(input("enter the value: "))
        while a < 0 :
                 print("wrong value")
                 a = int(input("enter the value: "))
        b = input("enter the catagory :")
        billbook[b] = a
        totalexpens.append(billbook)
        totalmoney.append(a)
    elif task == "view exp":
        if totalexpens == [] :
            print("nothing is listed")
        else:
            print(totalexpens)
    elif task == "total":
         print(sum(totalmoney))
    elif task == "remove exp":
        if totalexpens == []:
            print("nothing in the list")
        elif totalexpens != []:
            print(totalexpens)
            remove = int(input("enter the entry no:"))
            totalexpens.remove(remove)
    if task == "exit":
        break
