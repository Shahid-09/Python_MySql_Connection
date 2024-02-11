from dbhelper import DBHelper  

def main():
    
    db = DBHelper()

    while True:
        print("**********Welcome**********")
        print()
        print("PRESS 1 to Insert new user: ")
        print("PRESS 2 to Display all user: ")
        print("PRESS 3 to Delete user: ")
        print("PRESS 4 to Update user: ")
        print("PRESS 5 to Exit programm: ")
        print()
        try:
            choice = int(input())
            if (choice == 1):
                # insert user
                UserId = int(input("Input UserId: "))
                UserName = input("Input Name: ")
                UserPhone = input("Input Phone No: ")
                db.insert_user(UserId, UserName, UserPhone)

            elif (choice == 2):
                # show user data 
                db.fetch_all() 

            elif (choice == 3):
                # delete user
                UserId = int(input("Delete UserId(user): "))
                db.delete_user(UserId)

            elif (choice == 4):
                # update user
                UserId = int(input("Enter UserId: "))
                NewName = input("Update Name: ")
                NewPhone = input("Update Phone No: ")
                db.update_user(UserId, NewName,NewPhone)

            elif (choice == 5):
                # exit program
                break

            else:
                print("Invalid Input ! Try Again: ")
                
        except Exception as e:
            # print(e)
            print("Invalid Details ! Try Again: ")

if __name__ == "__main__": # If this file module __name__ is 'main' then run this program.We use this condition because we import module ############################ and we don't want to run all file we want only run main function when it's call..
    main()




                
            

