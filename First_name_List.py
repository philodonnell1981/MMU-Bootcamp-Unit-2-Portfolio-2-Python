def main_menu(user_choice):
    print("(1) Show Names")
    print("(2) Add Name")
    print("(3) Change Name")
    print("(4) Remove Name")
    print("(5) Exit")

def show_first_names():
    print(names)

def add_name(name_to_add):
    names.append(name_to_add)
    print(names)

def change_name():
    pass

def remove_name():
    pass

def exit():
    pass

names=[]
user_choice=int(input("Enter a selection (1-5) from the menu above:"))
main_menu(user_choice)

if(user_choice == 1):
    show_first_names()
elif(user_choice== 2):
    name_to_add = input("Enter a name to add:")
    add_name(name_to_add)
elif(user_choice== 3):
    change_name()
elif(user_choice== 4):
    remove_name()
else:
    exit()
