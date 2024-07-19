def main():
    emps = int(input("How many employee Records do you want to creat? "))
    employee_file_write = open("File Handling/Task 02/emploee.txt","a")
    for n in range(1, emps + 1):
        
        print("Enter the Data for Employee #",n)
        
        name = input("Name: ")
        id = input("ID Number: ")
        dep = input("Department: ")
        
        employee_file_write.write("Name: "+str(name)+"\n")
        employee_file_write.write("ID Number: "+str(id)+"\n")
        employee_file_write.write("Department: "+str(dep)+"\n")
        
    employee_file_write.close()
    
    print("Data Entered Sucessfully")
    
    employee_file_read = open("File Handling/Task 02/emploee.txt","r")
    
    name = employee_file_read.readline()
    
    while name != "":
        id = employee_file_read.readline()
        dep = employee_file_read.readline()
        
        n = name.strip("\n")
        i = id.strip("\n")
        d = dep.strip("\n")
        
        print(n)
        print(i)
        print(d)
        
        name = employee_file_read.readline()
    
    employee_file_read.close()
        
main()      