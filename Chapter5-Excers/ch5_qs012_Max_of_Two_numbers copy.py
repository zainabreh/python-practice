import random
def main():
    for count in range(10):
        print("Question No:",count+1,"\n")
        print(random.randint(1,10)," + ", random.randint(1,10)," = __________\n")
        
main()