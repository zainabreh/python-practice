import random


def main():
    cp_choice = computer_choice()
    result(cp_choice)


def computer_choice():
    ran = random.randint(1, 3)
    return ran


def user_choice():
    us = int(input("1).Rock\n2).Paper\n3).Scissor\n4).Quit\n Enter Your Choice"))
    return us


def result(c):
        while True:
            u = user_choice()
            ch = 4
            if(u == ch):
                    print("See you Next Time......Byee")
                    break
            if c == 1 and u == 1 or c == 2 and u == 2 or c == 3 and u == 3:
                    print("It's Draw!!!")
            
            elif c == 1 and u == 2:
                print("Computer Choice is: Rock \nYour choice is: Paper\n")
                print("You WIN!!!")
            
            elif c == 1 and u == 3:
                print("Computer Choice is: Rock \nYour choice is: Scissor\n")
                print("Computer WIN......")
            elif c == 2 and u == 3:
                print("Computer Choice is: Paper \nYour choice is: Scissor\n")
                print("You WIN!!!")
            
            elif c == 2 and u == 1:
                print("Computer Choice is: Paper \nYour choice is: Rock\n")
                print("Computer WIN......")
            elif c == 3 and u == 1:
                print("Computer Choice is: Scissor \nYour choice is: Rock\n")
                print("You WIN!!!")
            
            elif c == 3 and u == 2:
                print("Computer Choice is: Scissor \nYour choice is: Paper\n")
                print("Computer WIN.....")
        
        
        
main()