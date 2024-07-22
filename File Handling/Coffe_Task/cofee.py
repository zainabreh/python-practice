import os

def main():
    
    # Adding Data
    # add_coffee()
    
    # Displaying Data
    # display_coffee()
    
    # Searching Data
    # searching_coffee()
    
    # Modify Records
    modify_coffee()
    

def add_coffee():
    
    try:
        coffee_file = open('Coffe_Task\cofee.txt','a')
        print("Enter the Coffee Data:\n")
        d = input("Enter Coffee Name: ")
        q = input("Enter Coffee Quantity: ")
    
        coffee_file.write("Description: " + str(d) + "\n")
        coffee_file.write('Quantity: ' + str(q) + "\n") 
    
        choice = input("Do you want to add more: y = yes & n = no: ")
    
        while choice != 'n':    
        
            d = input("Enter Coffee Name: ")
            q = input("Enter Coffee Quantity: ")
    
            choice = input("Do you want to add more: y = yes & n = no") 
        
            coffee_file.write("Description: " + str(d) + "\n")
            coffee_file.write('Quantity: ' + str(q) + "\n")  
        coffee_file.close()
    except Exception as er:
        print("Error Occured:", er)
                
def display_coffee():
    try:
        with open('Coffe_Task\cofee.txt','r') as coffee_file:
    
            reading = coffee_file.readlines()
        
            for line in reading:
                data = line.rstrip('\n')
                print(data)
    except IOError:
        print("Error: Couldn't read file" + 'Coffe_Task\cofee.txt')

def searching_coffee():
  query = input("Enter a Description to search for: ")
  found = False
  with open('Coffe_Task\cofee.txt','r') as coffee_file:
    for line in coffee_file:
        
        if query.lower() in line.lower():
            found = True
            print("Item Found......\n\n\n")
            
            quantity = next(coffee_file,None)
            
            if quantity:
                print(line.rstrip())
                print(quantity.rstrip())
                
            else:
                print("End of File")
            break
        
    if not found:
        print("Not Found....")


# Sequentially Modification

def modify_coffee():
    
    found = False
    
    query = input("Enter the Description: ")
    new_quantity = int(input("Enter New Quantity: "))
        
    with open('Coffe_Task\cofee.txt','r') as file , open('Coffe_Task\ temp_cofee.txt','w') as temp:
    
        for line in file:
            if query.lower() in line.lower() or query.lower() in line.lower()[0]:
                found = True
                q = next(file,None)
                
                if q:
                    temp.write(line)
                    temp.write("Quantity: "+str(new_quantity)+"\n")
                else:
                    print("End of file")
            else:
                temp.write(line)
                
        
        if found:
            print("File updated Successfully")
            
        else:
            print("Item not Found")
                        
    os.remove('Coffe_Task\cofee.txt')
    os.replace('Coffe_Task\ temp_cofee.txt','Coffe_Task\cofee.txt')



if  __name__ == "__main__":
    main()
