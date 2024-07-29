def main():
    numbers = [74,19,105,20,-2,67,77,124,-45,38]
    valid_Number = []
    
    for i in numbers:
        if i > 0 and i < 100:
            valid_Number.append(i)
    
    for j in valid_Number:
        print(j)
        
    
    
main()