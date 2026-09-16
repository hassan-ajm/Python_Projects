contact = {}
def add_contact():
  name = input("Name:")
  phone = input("Ph#: ")# learned that u cant use # , like Ph# it will make rest commented omut 
  email = input("Email: ")
  contact[name]= {"Ph#":phone , "Email":email}
  print(F"{name} is added with {phone} and {email}")


def search_contact():
  name=input("Enter the name to search:")
  info=contact.get(name)
  if info:
    print(f"Ph#:{info['Ph#']} , Email:{info['Email']} ")
  else:
    print("No Such Contact Exist")


def delete_contact():
  name=input("Enter the name of the contact to Delete:")
  if contact.pop(name ,None) is not None:
    print (f"{name} has been delete sucessfully")
  else:
    print(f"NO such contact exist with the name :{name}")


def display_allcontacts():
  if not contact:
    print("Currenlty the Book is Empty Please Enter some name ")
  else:
    for name,info in contact.items():
      print(f"{name}: {info['Ph#']} , {info['Email']}")#this \"\" is causing issue after the first \ all the rest become a non code thing so we use ''

print("#############################################################")
print("#                      Welcome !                            #")
print("#                                                           #")
print("#                    To Digital CLI                         #")
print("#                                                           #")
print("#                      PHONE BOOK                           #")
print("#                                                           #")
print("#############################################################")
while True:
    print("\n1) Add  2) Search  3) Delete  4) List  q) Quit")
    choice = input("Choice: ")
    if   choice == "1": add_contact()
    elif choice == "2": search_contact()
    elif choice == "3": delete_contact()
    elif choice == "4": display_allcontacts()
    elif choice == "q": break
    else: print("Invalid.")
