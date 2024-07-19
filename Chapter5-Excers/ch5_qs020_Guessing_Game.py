import random

def main():
    random_generator()
    
def random_generator():
    ran = random.randint(1,100)
    count = 0
    while True:
        count = count + 1
        user = int(input("Guess the Number between 1 - 100: ")) 
        if 0 <= user <= 100:
            print("Enter between 1 - 100: ")
            if user < ran:
                print("Too Low,Try again")
            elif user > ran:
                print("Too high,Try again")
            elif user == ran:
                print("Congrats,You Found It\n")
                print("You make ", count, "Guesses")
                break
                
                
        else:
            print("Out of Range")
main()