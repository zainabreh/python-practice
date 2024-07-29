def main():
    print("Enter 20 Numbers:")
    
    list = []
    sum = 0
    
    for i in range(20):
        user_input = input()
        list.append( user_input)
        
    print("Minimum Number in the List is",min(list))
    print("Maximum Number in the List is",max(list))
        
    for i in list:
        sum += int(i)
        
    print("Sum of the Numbers is",sum)  
    
    avg = sum/len(list) 
    
    print("Average of the Number is:",avg)
    
main()