import random
def main():
    
    number_generator()
    
def number_generator():
    odd = 0
    even = 0
    for count in range(1,100):
        ran = random.randint(1,100)
        if ran % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1 
    
    print("No.of Even Numbers in 1 - 100 is: ",even)
    print("No.of odd Numbers in 1 - 100 is: ",odd)
    
main()   
            
        