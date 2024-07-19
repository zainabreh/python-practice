def main():
    # num_days = int(input("For how many days you have sales:"))
    
    # sales_file = open('File Handling/p2/sales.txt','a')
    
    # for count in range(1,num_days + 1):
    
    #     sales = float(input("Enter the sales for day #" + str(count) + ":"))
        
    #     sales_file.write(str(sales) + '\n')
        
    # sales_file.close()
    
    print("Data is written")
    
    
    read = open('File Handling/p2/sales.txt','r')
    
    # r = read.readline()
    
    
    # 1 way to read data from file using loop this one is not good
    
    
    # while r != " ":
    #     amount = float(r)
    #     print(amount)
    #     r = read.readline()
    
    
    
    
    
    
    # 2 way to read data from file using loop this one is good

    
    
    for c in read:
        r = float(c)
        print(r)
        
    read.close()
    
main()