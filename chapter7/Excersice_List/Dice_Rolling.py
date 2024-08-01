import random
def main():
    
    no_rolls = int(input("Enter Positive Number: "))
    
    roll(no_rolls)
    
def roll(rolla):
    rand_list = []
    
    for i in range(rolla):
        generate_random = random.randint(1,6)
        rand_list.append(generate_random)
        
    print(" ".join(map(str,rand_list)))
        
main()