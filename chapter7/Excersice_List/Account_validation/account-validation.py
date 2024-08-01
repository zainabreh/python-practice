def main():
    list_Number = []
    
    with open("Account_validation/account.txt",'r') as file:
        for i in file:
            list_Number.append(i.strip())
            
    print("Enter charge account number:")
    inp = input()
        
    if inp in list_Number:
        print("Valid...")
    else:
        print("Invalid")        
            
main()