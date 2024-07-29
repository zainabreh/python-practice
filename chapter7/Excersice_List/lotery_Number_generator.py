import random
def main():
    
    li = []*7
    
    for i in range(7):
        ran = random.randint(0,9)
        li.append(ran)
        
    for j in li:
        print(j)
    
    
main()    